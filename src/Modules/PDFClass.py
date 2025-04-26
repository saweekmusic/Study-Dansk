from src.Modules.WordClass import Word, WORDS
from src.Modules.MeaningClass import Meaning
from src.Modules.IdiomClass import Idiom
from fpdf import FPDF
from src.Constants import TOPIC, LEVEL
import random
import re
from wordsearch import WordSearch, Alphabets

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


    def print_title(self, title: str):
        self.set_font(family='helvetica-neue', style='B', size=30)
        self.write(text=title)
        self.ln()
        self.ln(2.0)

        # Print the line under the title
        with self.local_context(line_width=0.5):
            self.set_draw_color(r=179, g=179, b=179)
            self.line(self.l_margin, 
                      self.get_y(), 
                      self.w - self.r_margin, 
                      self.get_y())
        
        self.ln(3)
        

    def print_subtitle(self, subtitle: str):
        self.ln(5)
        gap = 1.5

        self.set_font(family='helvetica-neue', style='B', size=18)
        self.cell(text=subtitle)

        with self.local_context(text_mode='STROKE', line_width=0.5):
            for i in range(0, 10):
                self.set_x(self.get_x() + gap)
                self.cell(text=subtitle)
        
        self.ln()
        self.ln(2.0)


    # Print_table function
    def print_table(self, meanings: list[Meaning]):

        # Set the font
        self.set_font('helvetica-neue', size=11, style='')

        # Follow the screenshot on your phone or on the website
        with self.table(first_row_as_headings=False, 
                        line_height=1.35 * self.font_size, 
                        v_align='TOP', 
                        padding=2, 
                        markdown=True) as table:

            for meaning in meanings:
                row = table.row()
                row.cell(meaning.definition_en)
                row.cell(f"**{meaning.example}** / {meaning.example_en}")
        self.ln(3)


    # Print definition function
    def print_definition(self, word: Word):

        # Set the font
        with self.local_context():

            # Set the font
            self.set_font(family='helvetica-neue', style='B', size=11)
            
            # Print the word
            self.cell(text=f'{word.determiner} {word.word}' if word.determiner else f'{word.word}')

        # Print the pronunciation
        self.set_font(family='helvetica-neue', style='', size=11)
        self.cell(text=word.pronunciation)
        self.set_x(self.get_x() + 2)

        # Get the width of the bending
        bendings = '[' + ', '.join(bending for bending in word.bendings) + ']'
        bending_width = self.get_string_width(bendings)

        # Get the height of the text
        height = self.font_size * 1.2

        # Subtract the line width
        height = height - 1.5

        # Print the line
        with self.local_context(line_width=0.5):
            line_length = self.w - self.get_x() - self.r_margin - bending_width - 2

            self.set_dash_pattern(dash=0.125, gap=4)
            self.set_draw_color(r=179, g=179, b=179)
            self.line(self.get_x(), 
                      self.get_y() + height, 
                      self.get_x() + line_length, 
                      self.get_y() + height)

        # Print the bendings
        self.set_x(self.get_x() + line_length + 2)
        self.cell(text=bendings)


    def print_words(self, words: str, pos: str):

        # For every word in the array words
        for word in words:

            # Create a new word object
            wordInit = Word(search_word=word, pos=pos)
            WORDS.append(wordInit)

            # Print the definition of the word
            self.print_definition(word=wordInit)

            # Gap
            self.ln()
            self.ln(2)

            # Print the table of meanings
            self.print_table(meanings=wordInit.meanings)

            # Set the gap between the words
            self.ln(5)


    def print_matches(self):
        words = []
        defs = []

        for word in WORDS:
            words.append(word.word)
            defs.append(word.meanings[0].definition_en)

        # Shuffle the words and definitions
        random.shuffle(words)
        random.shuffle(defs)

        # Set the font
        self.set_font('helvetica-neue', size=11, style='')

        # Create a table
        with self.table(first_row_as_headings=False, 
                        line_height=1.35 * self.font_size, 
                        v_align='M',
                        gutter_height=3, 
                        gutter_width=20,
                        col_widths=(1, 2),
                        padding=2, 
                        markdown=True) as table:

            # Add the rows
            for i, word in enumerate(words):
                row = table.row()
                row.cell(word, align='C')
                row.cell(defs[i], align='C')

        self.ln(8)
    

    def print_fix_words(self):
        words = [word.word for word in WORDS]
        random.shuffle(words)

        #Shuffle letters in the words
        for i, word in enumerate(words):
            letters = list(word)
            random.shuffle(letters)
            words[i] = ''.join(letters)

        # Set the font
        self.set_font('helvetica-neue', size=11, style='')

        # Create a table
        with self.table(first_row_as_headings=False, 
                        line_height=1.35 * self.font_size, 
                        v_align='M',
                        padding=2,
                        borders_layout='NONE',
                        markdown=True) as table:

            # Add the rows
            for i, word in enumerate(words):
                row = table.row()
                row.cell(word, align='L')
                row.cell('', align='L', border='BOTTOM')


    def create_puzzle(self):
        words = [word.word for word in WORDS]

        # Set the font
        self.set_font('helvetica-neue', size=11, style='')

        # Create a word search puzzle
        puzzle = WordSearch(words=words, language=Alphabets.DANISH)

        with self.table(first_row_as_headings=False, 
                        borders_layout='ALL') as table:
            
            # Add the rows
            for row in puzzle.grid:
                table_row = table.row()
                for cell in row:
                    table_row.cell(cell, align='C', v_align='M', border='NONE')
            
            
