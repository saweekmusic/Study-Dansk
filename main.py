from src.Modules.Section import Section
from src.Modules.PDFClass import PDF
import src.Config as config
from src.Modules.WordClass import Word


pdf = PDF()
pdf.add_page()
WORDS: list[Word] = []

for section in config.titles.keys():
    Section(
        pdf, 
        config.titles[section], 
        config.descriptions[section],
        config.contents[section](pdf, WORDS)).render()

# Section 5: Fill from the box
# Section 6: Idioms
# Section 7: Write a letter
# Section 8: Answers for 'Fill in the Blanks'

pdf.output('Output/output.pdf')