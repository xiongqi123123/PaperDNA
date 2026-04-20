from reportlab.pdfgen import canvas

def create_pdf(filename):
    c = canvas.Canvas(filename)
    c.drawString(100, 750, "Hello MinerU!")
    c.drawString(100, 730, "This is a test PDF for layout analysis.")
    c.drawString(100, 710, "Table 1: Test Table")
    c.drawString(100, 690, "Col1  Col2  Col3")
    c.drawString(100, 670, "Val1  Val2  Val3")
    c.save()

if __name__ == "__main__":
    create_pdf("test.pdf")
    print("Created test.pdf")
