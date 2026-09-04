
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "qwen/qwen3.8-27b"


def generate_summary(text, summary_length):

    prompt = f"""
You are an expert AI document summarizer.

Summarize the following document.

Summary Length: {summary_length}

Rules:
- Use simple English.
- Use bullet points.
- Do not invent information.
- Keep only the important points.

Document:

{text}
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are an expert document summarizer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_tokens=800
    )

    return response.choices[0].message.content