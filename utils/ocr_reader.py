
import pytesseract
from pdf2image import convert_from_bytes

# Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Poppler path
POPPLER_PATH = r"C:\poppler\poppler-26.02.0\Library\bin"


def extract_text_from_scanned_pdf(uploaded_file):
    """
    Extract text from scanned PDFs using OCR.
    """

    images = convert_from_bytes(
        uploaded_file.read(),
        poppler_path=POPPLER_PATH
    )

    text = ""

    for image in images:
        text += pytesseract.image_to_string(image)
        text += "\n"

    return text