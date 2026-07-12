
from utils.pdf_reader import extract_text


def extract_multiple_documents(uploaded_files):
    """
    Extracts text from multiple uploaded documents
    and combines them into one string.
    """

    combined_text = ""

    for uploaded_file in uploaded_files:

        try:

            text = extract_text(uploaded_file)

            combined_text += f"\n\n========== {uploaded_file.name} ==========\n\n"

            combined_text += text

        except Exception as e:

            combined_text += (
                f"\n\nCould not read {uploaded_file.name}\n"
            )

    return combined_text