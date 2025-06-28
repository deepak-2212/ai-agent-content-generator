import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_content(prompt: str, content_type: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful AI content creator."},
            {"role": "user", "content": f"Write a {content_type} for: {prompt}"}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content
