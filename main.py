from src.Modules.PDFClass import PDF
from src.Functions.AIrequests import *

pdf = PDF()
pdf.add_page()

# Section 1
pdf.print_title("Section 1: Learning New Words")
pdf.print_subtitle("Verbs")
pdf.print_words(askWordsAI(None, "DU1.5", "math", "verb"), "verb")

# Section 2
pdf.print_title("Section 2: Match the Words")
pdf.print_matches()

# Section 3: Put the letter in the right order
pdf.print_title("Section 3: Fix the Words")
pdf.print_fix_words()

# Section 4: Find Words (a puzzle)
pdf.print_title("Section 4: Find the Words")
pdf.create_puzzle()

# Section 5: Fill from the box
# Section 6: Idioms
# Section 7: Write a letter
# Section 8: Answers for 'Fill in the Blanks'



pdf.output("Output/output.pdf")