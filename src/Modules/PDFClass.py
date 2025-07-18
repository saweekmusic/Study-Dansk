from src.Modules.TableClass import CustomTable
from src.Modules.WordClass import Word, WORDS
from src.Modules.MeaningClass import Meaning
from fpdf import FPDF
import random
from wordsearch import WordSearch, Alphabets
from src.Functions.AIrequests import *

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
        self.set_left_margin(15)
        self.set_right_margin(15)
        self.set_top_margin(15)

        self.add_font('helvetica-neue', 
                      style='', 
                      fname='src/Fonts/HelveticaNeue-01.ttf',
                      uni=True)
        self.add_font('helvetica-neue', 
                      style='B', 
                      fname='src/Fonts/HelveticaNeue-Bold-02.ttf',
                      uni=True)
        self.add_font('helvetica-neue', 
                      style='I', 
                      fname='src/Fonts/HelveticaNeue-Italic-03.ttf',
                      uni=True)
        self.add_font('helvetica-neue', 
                      style='BI', 
                      fname='src/Fonts/HelveticaNeue-BoldItalic-04.ttf',
                      uni=True)

#     def print_matches(self):
#         words = []
#         defs = []

#         for word in WORDS:
#             words.append(word.word)
#             defs.append(word.meanings[0].definition_en)

#         # Shuffle the words and definitions
#         random.shuffle(words)
#         random.shuffle(defs)

#         # Set the font
#         self.set_font('helvetica-neue', size=11, style='')

#         # Create a table
#         with self.table(first_row_as_headings=False, 
#                         line_height=int(1.35 * self.font_size), 
#                         v_align='M',
#                         gutter_height=3, 
#                         gutter_width=20,
#                         col_widths=(1, 2),
#                         padding=2, 
#                         markdown=True) as table:

#             # Add the rows
#             for i, word in enumerate(words):
#                 row = table.row()
#                 row.cell(word, align='C')
#                 row.cell(defs[i], align='C')

#         self.section_gap()
    

#     def print_fix_words(self):
#         words = [word.word for word in WORDS]
#         random.shuffle(words)

#         #Shuffle letters in the words
#         for i, word in enumerate(words):
#             letters = list(word)
#             random.shuffle(letters)
#             words[i] = ''.join(letters)

#         # Set the font
#         self.set_font('helvetica-neue', size=11, style='')

#         # Create a table
#         with self.table(first_row_as_headings=False, 
#                         line_height=int(1.35 * self.font_size), 
#                         v_align='M',
#                         padding=2,
#                         borders_layout='NONE',
#                         markdown=True) as table:

#             # Add the rows
#             for i, word in enumerate(words):
#                 row = table.row()
#                 row.cell(word, align='L')
#                 row.cell('', align='L', border='BOTTOM')

#         self.section_gap()


#     def create_puzzle(self):
#         words = [word.word for word in WORDS]

#         # Set the font
#         self.set_font('helvetica-neue', size=11, style='')

#         # Create a word search puzzle
#         puzzle = WordSearch(words=words, language=Alphabets.DANISH)

#         table = CustomTable(fpdf=self, first_row_as_headings=False, 
#                         borders_layout='ALL')
            
#         # Add the rows
#         for row in puzzle.grid:
#             table.row(row)

#         table_height = int(table.get_total_height())

#         with self.table(first_row_as_headings=False, 
#                         borders_layout='ALL', width=table_height) as render_teble:
#             # Add the rows
#             for row in puzzle.grid:
#                 table_row = render_teble.row()
#                 for cell in row:
#                     table_row.cell(cell, align='C', v_align='M', border='NONE')

#         self.section_gap()


#     def print_gap(self, gap: int):
#         self.ln()
#         self.ln(gap)
            

#     # Gap between the sections
#     def section_gap(self):
#         self.ln(10)


    