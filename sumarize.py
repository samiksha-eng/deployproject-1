import os
from dotenv import load_dotenv
from google import genai

# Load variables from .env
load_dotenv()

# Read API key securely
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY is missing. Check your .env file."
    )

# Create Gemini client
client = genai.Client(api_key=api_key)
article="""Artificial Intelligence (AI) refers to computer systems and software built to mimic human-like intelligence, such as learning, reasoning, and solving complex problems. Rooted in early computer science concepts from the mid-20th century, the field relies on massive amounts of data and advanced algorithms to find patterns. Today, it spans multiple branches, including machine learning, deep learning, and natural language processing, which allow machines to adapt and improve over time without explicit step-by-step programming.
In daily life and global industries, AI drives major innovations across healthcare, finance, education, and transportation. Doctors use AI tools for faster medical diagnostics and drug discovery, while financial institutions rely on it to catch fraudulent transactions in real time. Furthermore, everyday tools like smartphone voice assistants, recommendation engines on streaming platforms, and autonomous navigation systems all operate on underlying AI frameworks.
"""
prompt=f"""
sumarize below article in 50 words
{article}
"""
response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=prompt
)

# Display response
print("\nGemini Response:\n")
print(response.text)