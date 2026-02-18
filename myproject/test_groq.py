import os
from dotenv import load_dotenv
from groq import Groq

# Manually load the env
base_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(base_dir, ".env")
load_dotenv(env_path, override=True)

api_key = os.getenv("GROQ_API_KEY")
api_base = os.getenv("OPENAI_API_BASE")
print(f"Testing key: {api_key[:10]}...{api_key[-5:]}")
print(f"Detected API Base: {api_base}")

client = Groq(api_key=api_key)

try:
    models = client.models.list()
    print("SUCCESS: Connection established! Found models.")
    for model in models.data[:3]:
        print(f" - {model.id}")
except Exception as e:
    print(f"FAILED: {e}")
