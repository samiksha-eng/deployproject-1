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
feedback="This prouduct is so good but its very epensive"

prompt=f""" 
classify customer feedback positive,negative,neutral and other
{feedback}
"""
response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=prompt
)

# Display response
print(response.text)