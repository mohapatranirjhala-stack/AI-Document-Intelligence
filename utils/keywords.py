
from collections import Counter
import re

STOP_WORDS = {
    "the", "a", "an", "and", "or", "is", "are", "was",
    "were", "to", "of", "in", "on", "for", "with",
    "this", "that", "it", "as", "at", "by", "from",
    "be", "has", "have", "had", "will", "can", "into",
    "using", "used", "also", "their", "its", "than"
}


def extract_keywords(text, top_n=10):

    words = re.findall(r"\b[A-Za-z]{3,}\b", text.lower())

    filtered = [
        word for word in words
        if word not in STOP_WORDS
    ]

    counts = Counter(filtered)

    return counts.most_common(top_n)