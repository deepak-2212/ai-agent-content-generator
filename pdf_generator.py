from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(content, output_path="output/output.pdf"):
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter
    text_object = c.beginText(40, height - 40)
    for line in content.split("\n"):
        text_object.textLine(line)
    c.drawText(text_object)
    c.save()
