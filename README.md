# Django Tweet Project

A simple but powerful Twitter-like application built with Django and Bootstrap. This project features full CRUD capabilities for tweets, user authentication, and a real-time search engine.

## 🚀 Features

- **User Authentication**: Secure Login, Logout, and Registration systems.
- **Tweet CRUD**: Users can Create, Read, Update, and Delete their own tweets.
- **Image Support**: Upload and display photos along with tweet content.
- **Search System**: Search tweets by content or author username.
- **Responsive Design**: Modern, side-by-side card layout built with Bootstrap 5 and Dark Mode support.
- **Permissions**: Only the original author can edit or delete their tweets.

## 🛠️ Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML5, Vanilla CSS, Bootstrap 5
- **Database**: SQLite (default)

## 🏃 How to Run Locally

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd djangoproject
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   *(Assuming you have a requirements.txt, if not install Django manually)*
   ```bash
   pip install django pillow
   ```

4. **Run migrations**:
   ```bash
   cd myproject
   python manage.py migrate
   ```

5. **Start the server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the app**:
   Open your browser and go to `http://127.0.0.1:8000`

## 📝 Final Submission
This project represents a complete implementation of a social media micro-blogging platform as part of a Django development learning path.
