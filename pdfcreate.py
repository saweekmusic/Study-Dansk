from wordclass import Word
from meanings import Meaning
from idioms import Idiom
from fpdf import FPDF

class PDF(FPDF):

    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
        self.set_left_margin(15)
        self.set_right_margin(15)
        self.set_top_margin(15)

        self.add_font('helvetica-neue', style='', fname='Fonts/HelveticaNeue-01.ttf')
        self.add_font('helvetica-neue', style='B', fname='Fonts/HelveticaNeue-Bold-02.ttf')
        self.add_font('helvetica-neue', style='I', fname='Fonts/HelveticaNeue-Italic-03.ttf')
        self.add_font('helvetica-neue', style='BI', fname='Fonts/HelveticaNeue-BoldItalic-04.ttf')


    def print_title(self, title: str):
        self.set_font(family='helvetica-neue', style='B', size=30)
        self.write(text=title)
        self.ln()
        self.ln(2.0)

        # Print the line under the title
        with self.local_context(line_width=0.5):
            self.set_draw_color(r=179, g=179, b=179)
            self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        
        self.ln(5)
        

    def print_subtitle(self, subtitle: str):
        gap = 1.5

        self.set_font(family='helvetica-neue', style='B', size=18)
        self.cell(text=subtitle)

        with self.local_context(text_mode='STROKE', line_width=0.5):
            for i in range(0, 10):
                self.set_x(self.get_x() + gap)
                self.cell(text=subtitle)

    # TODO: Finish the print_table function
    def print_table(self, meanings: list[Meaning]):
        # Set the font

        # Follow the screenshot on your phone or on the website
        pass

    # TODO: Finish the print_definition function
    def print_definition(self, word: Word):
        # Set the font
        with self.local_context(font_family='helvetica-neue', font_size=11, font_style='B'):

            # Print the determiner if it exits
            if word.determiner:
                self.write(text=f'{word.determiner} ')
            
            # Print the word
            self.write(text=f'{word.word}')

        # Print the pronunciation
        self.set_font(family='helvetica-neue', style='', size=11)
        self.write(text=word.pronunciation)
        self.set_x(self.get_x() + 2)

        bendings = '[' + ', '.join(bending for bending in word.bendings) + ']'

        # Print the dot line
        bending_width = self.get_string_width(bendings)
        with self.local_context(line_width=0.5):
            line_length = self.w - self.get_x() - self.r_margin - bending_width - 2
            self.set_draw_color(r=179, g=179, b=179)
            self.line(self.get_x(), self.get_y(), self.get_x() + line_length, self.get_y())

        # Print the bendings
        self.cell(text=bendings)

        # Set the gap between the definition and the table of meanings

        pass


    def print_words(self, words: str, pos: str):

        # For every word in the array words
        for word in words:

            # Create a new word object
            wordInit = Word(search_word=word, pos=pos)

            # Print the definition of the word
            self.print_definition(word=wordInit)

            # Print the table of meanings
            self.print_table(meanings=wordInit.meanings)

            # Set the gap between the words
            self.ln(10)