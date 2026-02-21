from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm,UserRegistrationForm,UserLoginForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .ai_service import refine_tweet_content, analyze_vibe, check_authenticity
import json

# Create your views here.

def index(request):
    return render(request, "index.html")

from django.db.models import Q

@login_required
def tweet_list(request):
    query = request.GET.get("search")
    if query:
        tweets = Tweet.objects.filter(
            Q(content__icontains=query) | Q(user__username__icontains=query)
        ).order_by("-created_at")
    else:
        tweets = Tweet.objects.all().order_by("-created_at")
    return render(request, "tweet_list.html", {"tweets": tweets, "query": query})

@login_required
def tweet_detail(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    return render(request, "tweet_detail.html", {"tweet": tweet})

@login_required
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.vibe = analyze_vibe(tweet.content)
            
            # Perform Fact-Check
            auth_result = check_authenticity(tweet.content)
            tweet.is_verified = auth_result.get('is_verified', False)
            tweet.authenticity_score = auth_result.get('score', 100)
            tweet.fact_check_reason = auth_result.get('reason', "")
            
            tweet.save()
            return redirect("tweet_list")
    else:
        form = TweetForm()
    return render(request, "tweet_create.html", {"form": form})

@login_required 
def tweet_update(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk,user=request.user)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.vibe = analyze_vibe(tweet.content)
            
            # Re-perform Fact-Check on update
            auth_result = check_authenticity(tweet.content)
            tweet.is_verified = auth_result.get('is_verified', False)
            tweet.authenticity_score = auth_result.get('score', 100)
            tweet.fact_check_reason = auth_result.get('reason', "")
            
            tweet.save()
            return redirect("tweet_list")
    else:
        form = TweetForm(instance=tweet)
    return render(request, "tweet_update.html", {"form": form})

@login_required
def tweet_delete(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk,user=request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect("tweet_list")
    return render(request, "tweet_delete.html", {"tweet": tweet})

from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            auth_login(request, user)
            return redirect("tweet_list")
    else:
        form = UserRegistrationForm()
    return render(request, "registration/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect("tweet_list")
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = UserLoginForm()
    return render(request, "registration/login.html", {"form": form})

def logout_view(request):
    auth_logout(request)
    return redirect("login")

@login_required
def refine_tweet(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            content = data.get("content", "")
            refined_content = refine_tweet_content(content)
            return JsonResponse({"refined_content": refined_content})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=405)
