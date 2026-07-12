
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(summary):

    pdf_path = "summary.pdf"

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph("<b>AI Document Summary</b>", styles["Heading1"])
    )

    story.append(
        Paragraph(summary.replace("\n", "<br/>"), styles["BodyText"])
    )

    doc.build(story)

    return pdf_path