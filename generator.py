from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_content(topic, content_type):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": f"You are a helpful AI that writes a {content_type}."},
            {"role": "user", "content": f"Write a {content_type} about: {topic}"}
        ]
    )
    return response.choices[0].message.content
