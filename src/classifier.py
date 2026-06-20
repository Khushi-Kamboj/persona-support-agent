import os
import json

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def classify_persona(user_message):

    prompt = f"""
You are an advanced customer persona classifier.

Classify the user into EXACTLY ONE category:

1. Technical Expert
2. Frustrated User
3. Business Executive

Return ONLY valid JSON.

Example:

{{
  "persona":"Technical Expert",
  "confidence":0.95,
  "reasoning":"User discusses APIs and technical issues."
}}

User Message:
{user_message}
"""

    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
        response_mime_type="application/json"
    )
)
    print(response.text)

    return json.loads(response.text)

if __name__ == "__main__":

    query = """
I've been trying to reset my password for hours and nothing works!
"""

    result = classify_persona(query)

    print(result)