# Django AI-Powered Tweet Platform

A modern social media platform built with Django, powered by the Groq Llama 3 API. This project goes beyond traditional micro-blogging by integrating advanced AI capabilities for content creation, sentiment analysis, and misinformation detection.

## 🚀 AI-Native Features

- **✨ Smart Tweet Refinement**: Users can instantly transform rough notes into engaging, professional, or funny tweets with optimized hashtags using Llama 3.3.
- **🌈 Automatic AI Vibe Check**: Every post is automatically analyzed by a Llama 3.1 8B agent to detect its "vibe" (e.g., 🚀 Inspiring, 😂 Funny, 🤖 Techy), adding a layer of rich metadata to the feed.
- **🛡️ AI Fake News & Safety Detector**: A reasoning-based fact-checking system (Llama 3.3 70B) that scans tweets for factual accuracy and harmful advice, assigning an authenticity score and specific reasoning to every post.
- **User Authentication**: Secure Login, Logout, and Registration systems.
- **Full CRUD & Search**: Complete management of tweets with real-time concept-based search.
- **Responsive Design**: Premium Dark Mode UI built with Bootstrap 5.

## 🛠️ Tech Stack

- **Backend**: Python, Django 6.x
- **AI Engine**: Groq Cloud API (Llama 3.3 70B & Llama 3.1 8B)
- **Frontend**: Bootstrap 5, Javascript (Fetch API)
- **Environment**: Python-Dotenv for secure secret management
- **VEM**: UV (High-performance Python project manager)

## 🏃 How to Run Locally

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd djangoproject
   ```

2. **Set up the Environment**:
   Create a `.env` file in the `myproject/` folder:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   ```

3. **Install dependencies & Run with UV**:
   ```bash
   uv run python manage.py migrate
   uv run python manage.py runserver
   ```

4. **Access the app**:
   Go to `http://127.0.0.1:8000`

## 📝 Learning Objectives
This project was developed to explore the intersection of Web Frameworks and Agentic AI. Key challenges overcome include:
- Managing asynchronous AI requests in a synchronous Django flow.
- Prompt engineering for safety and misinformation detection.
- Handling environment conflicts and secure API key management.
