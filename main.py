from pdfcreate import PDF
from aifuncs import *

pdf = PDF()
pdf.add_page()
pdf.print_title("Section 1: Learning New Words")
pdf.print_subtitle("Verbs")
pdf.print_words(words=askWordsAI(None, "DU1.5", "math", "verb"), pos="verb")

pdf.output("output.pdf")