from fpdf import FPDF
import glob

from pathlib import Path

filepaths = glob.glob('files/*txt')

pdf = FPDF(orientation="P", format="A4", unit="mm")

for filepath in filepaths:
    filename = Path(filepath).stem.upper()
    # Read Content from the file
    pdf.add_page()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=0, h=16, txt=filename, ln=1, border=0, align="L")

    with open(filepath, "r") as file:
        content = file.read()

    pdf.set_font(family="Times", size=10)
    pdf.multi_cell(w=0, h=10, txt=content, align="L")
pdf.output("output.pdf")




