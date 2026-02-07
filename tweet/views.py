from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404, redirect
# Create your views here.

def index(request):
    return render(request, "index.html")

def tweet_list(request):
    tweets = Tweet.objects.all().order_by("-created_at")
    return render(request, "tweet_list.html", {"tweets": tweets})

def tweet_detail(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    return render(request, "tweet_detail.html", {"tweet": tweet})

def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("tweet_list")
    else:
        form = TweetForm()
    return render(request, "tweet_create.html", {"form": form})

def tweet_update(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk,user=request.user)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("tweet_list")
    else:
        form = TweetForm(instance=tweet)
    return render(request, "tweet_update.html", {"form": form})

def tweet_delete(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk,user=request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect("tweet_list")
    return render(request, "tweet_delete.html", {"tweet": tweet})