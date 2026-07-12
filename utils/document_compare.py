
from difflib import SequenceMatcher


def compare_documents(text1, text2):
    """
    Compare two documents and return:
    - similarity percentage
    - added lines
    - removed lines
    """

    similarity = SequenceMatcher(
        None,
        text1,
        text2
    ).ratio() * 100

    lines1 = set(text1.splitlines())

    lines2 = set(text2.splitlines())

    added = sorted(
        list(lines2 - lines1)
    )

    removed = sorted(
        list(lines1 - lines2)
    )

    return {
        "similarity": round(similarity, 2),
        "added": added,
        "removed": removed
    }