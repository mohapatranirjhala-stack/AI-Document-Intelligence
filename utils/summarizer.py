import os
import time
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "qwen/qwen3.8-27b"

# Keep comfortably below the 7,000 input-token limit.
# This is an approximate character-based chunk size.
CHUNK_SIZE = 16000


def summarize_chunk(text, summary_length):
    prompt = f"""
You are an expert AI document summarizer.

Summarize the following section of a document.

Summary Length: {summary_length}

Rules:
- Use simple English.
- Use bullet points.
- Do not invent information.
- Keep only the important points.
- Preserve important names, numbers, dates, facts, and conclusions.
- Summarize only information present in the provided text.

Document Section:

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


def generate_summary(text, summary_length):

    # For smaller documents, use the original single-request approach.
    if len(text) <= CHUNK_SIZE:
        return summarize_chunk(text, summary_length)

    # Split large documents into manageable sections.
    chunks = [
        text[i:i + CHUNK_SIZE]
        for i in range(0, len(text), CHUNK_SIZE)
    ]

    chunk_summaries = []

    for i, chunk in enumerate(chunks):
        summary = summarize_chunk(chunk, summary_length)
        chunk_summaries.append(summary)

        # Avoid sending multiple large requests too quickly.
        if i < len(chunks) - 1:
            time.sleep(2)

    # Combine the individual summaries.
    combined_text = "\n\n".join(
        f"Section {i + 1} Summary:\n{summary}"
        for i, summary in enumerate(chunk_summaries)
    )

    final_prompt = f"""
You are an expert AI document summarizer.

Create one final summary from the section summaries below.

Summary Length: {summary_length}

Rules:
- Use simple English.
- Use bullet points.
- Remove repetition between sections.
- Keep the most important information.
- Preserve important facts, numbers, dates, names, and conclusions.
- Do not invent information.
- Do not mention that the document was divided into sections.
- Return only the final summary.

Section Summaries:

{combined_text}
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
                "content": final_prompt
            }
        ],
        temperature=0.3,
        max_tokens=800
    )

    return response.choices[0].message.content