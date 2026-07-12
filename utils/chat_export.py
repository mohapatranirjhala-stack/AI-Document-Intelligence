
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph


def export_chat_pdf(chat_history, output_file="chat_history.pdf"):
    """
    Export chat history to PDF.
    """

    doc = SimpleDocTemplate(output_file)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph("<b>AI Document Intelligence - Chat History</b>", styles["Title"])
    )

    story.append(
        Paragraph("<br/><br/>", styles["Normal"])
    )

    for question, answer, snippets in chat_history:

        story.append(
            Paragraph(f"<b>You:</b> {question}", styles["Heading2"])
        )

        story.append(
            Paragraph(f"<b>AI:</b> {answer}", styles["BodyText"])
        )

        story.append(
            Paragraph("<br/>", styles["Normal"])
        )

    doc.build(story)

    return output_file


def export_chat_markdown(chat_history):

    markdown = "# AI Document Intelligence Chat History\n\n"

    for question, answer, snippets in chat_history:

        markdown += f"## You\n{question}\n\n"

        markdown += f"## AI\n{answer}\n\n"

        markdown += "---\n\n"

    return markdown