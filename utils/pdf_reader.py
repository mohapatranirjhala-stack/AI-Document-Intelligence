
import pdfplumber
import docx

from utils.ocr_reader import extract_text_from_scanned_pdf


def extract_pdf(file):

    text = ""

    with pdfplumber.open(file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    # If no text was extracted, use OCR
    if text.strip() == "":

        file.seek(0)

        text = extract_text_from_scanned_pdf(file)

    return text


def extract_docx(file):

    document = docx.Document(file)

    text = ""

    for paragraph in document.paragraphs:

        text += paragraph.text + "\n"

    return text


def extract_txt(file):

    return file.read().decode("utf-8")


def extract_text(file):

    extension = file.name.split(".")[-1].lower()

    if extension == "pdf":
        return extract_pdf(file)

    elif extension == "docx":
        return extract_docx(file)

    elif extension == "txt":
        return extract_txt(file)

    else:
        return ""