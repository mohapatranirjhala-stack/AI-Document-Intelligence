
from utils.summarizer import generate_summary


def generate_meeting_notes(document_text):
    """
    Generate structured meeting notes.
    """

    prompt = f"""
You are an AI meeting assistant.

Analyze the following meeting notes and return your response in this exact format.

## Meeting Summary
(2-3 paragraph summary)

## Action Items
- item 1
- item 2
- item 3

## Decisions
- decision 1
- decision 2

## Next Steps
- next step 1
- next step 2

Meeting Notes:

{document_text}
"""

    return generate_summary(prompt, "Long")