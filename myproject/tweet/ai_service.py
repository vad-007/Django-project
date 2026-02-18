from groq import Groq
from django.conf import settings

def refine_tweet_content(content):
    """
    Uses Groq LLM to refine tweet content, improve grammar, and add hashtags.
    """
    if not content:
        return ""

    print(f"DEBUG: Using API Key in service: {settings.GROQ_API_KEY[:7]}...{settings.GROQ_API_KEY[-4:]}")
    client = Groq(api_key=settings.GROQ_API_KEY)
    
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful social media assistant. Your task is to refine the user's tweet to make it more engaging, professional, or funny depending on context. Keep it concise (under 200 chars if possible) and add 2-3 relevant hashtags at the end. Only return the refined tweet text."
                },
                {
                    "role": "user",
                    "content": f"Refine this tweet: {content}"
                }
            ],
            model="llama-3.3-70b-versatile", # or another model like llama3-8b-8192
        )
        return chat_completion.choices[0].message.content.strip()
    except Exception as e:
        error_msg = f"Error calling Groq API: {e}"
        print(error_msg)
        return f"Error: {str(e)}"  # Modified to show error in frontend

def analyze_vibe(content):
    """
    Uses Groq LLM to determine the 'vibe' of a tweet.
    Returns a short string like '🚀 Inspiring' or '😂 Funny'.
    """
    if not content:
        return ""

    client = Groq(api_key=settings.GROQ_API_KEY)
    
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a social media analyst. Analyze the vibe of the tweet provided. Reply with ONLY one emoji and one word that best describes the sentiment (e.g., '🔥 Trendy', '🧐 Serious', '🎉 Festive', '😢 Sad', '😡 Angry', '🤖 Techy'). Keep it under 15 characters total."
                },
                {
                    "role": "user",
                    "content": f"Analyze this tweet: {content}"
                }
            ],
            model="llama-3.1-8b-instant", # Using a smaller/faster model for quick tagging
        )
        return chat_completion.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error calling Groq API for vibe: {e}")
        return "✨ Neutral"
