from fpdf.enums import Align
from fpdf.table import Table

from src.Constants import BODY_SIZE
from src.Constants import WORDS
from src.Functions.AIrequests import askWordsAI
from src.Functions.Calculate import table_height
from src.Modules.PDFClass import PDF
from src.Modules.WordClass import Word


class Body:
    def render(self):
        raise NotImplementedError("Subclasses should implement this method")


class TableContent(Body):
    def __init__(self, pdf: PDF, rows: list[list[str]], table: Table, square: bool = False) -> None:
        self.pdf = pdf
        self.rows = rows
        self.table = table

        # Setting the table
        for row in rows:
            self.table.row(row)

        if square:
            self.table._width = table_height(self.pdf, self.table) # type: ignore
            self.table._text_align = Align.coerce('C') # type: ignore

    def render(self):
        self.pdf.set_font(family = 'helvetica-neue', style = '', size = BODY_SIZE)
        self.table.render()


class TextContent(Body):
    def __init__(self, pdf: PDF, text: str) -> None:
        self.pdf = pdf
        self.text = text

    def render(self):
        self.pdf.set_font(family = 'helvetica-neue', style = '', size = BODY_SIZE)
        self.pdf.write(text = self.text)


class WordContent(Body):
    def __init__(self, pdf: PDF, DUlevel: str, topic: str, pos: str) -> None:
        self.pdf = pdf
        self.pos = pos
        self.words = askWordsAI(DUlevel, topic, self.pos)

    def subtitle(self):
        horizontal_gap = 1.5

        self.pdf.set_font(family = 'helvetica-neue', style = 'B', size = 18)
        self.pdf.cell(text = self.pos.capitalize())

        with self.pdf.local_context(text_mode = 'STROKE', line_width = 0.5):
            for i in range(0, 10):
                self.pdf.set_x(self.pdf.get_x() + horizontal_gap)
                self.pdf.cell(text = self.pos.capitalize())
        self.pdf.ln(3)

    def wordInfo(self, word: Word):
        # Print the word
        self.pdf.ln(5)
        self.pdf.set_font(family = 'helvetica-neue', style = 'B', size = BODY_SIZE)
        self.pdf.cell(text = f'{word.determiner} {word.word}' if word.determiner else f'{word.word}')

        # Print the pronunciation
        self.pdf.set_font(family = 'helvetica-neue', style = '', size = 11)
        self.pdf.cell(text = word.pronunciation)
        self.pdf.set_x(self.pdf.get_x() + 2)

        # Calculate the line width
        bendings = '[' + ', '.join(bending for bending in word.bendings) + ']'
        bending_width = self.pdf.get_string_width(bendings)
        height = self.pdf.font_size * 1.2
        height = height - 1.5
        line_length = self.pdf.w - self.pdf.get_x() - self.pdf.r_margin - bending_width - 2

        # Print the line
        with self.pdf.local_context(line_width = 0.5):
            self.pdf.set_dash_pattern(dash = 0.125, gap = 4)
            self.pdf.set_draw_color(r = 179, g = 179, b = 179)
            self.pdf.line(
                self.pdf.get_x(), 
                self.pdf.get_y() + height, 
                self.pdf.get_x() + line_length, 
                self.pdf.get_y() + height)

        # Print the bendings
        self.pdf.set_x(self.pdf.get_x() + line_length + 2)
        self.pdf.cell(text = bendings)

    def render(self):
        self.subtitle()

        for current_word in self.words:
            WORDS.append(current_word)

            word = Word(search_word=current_word, pos=self.pos)
            self.wordInfo(word)

            self.pdf.ln()
            self.pdf.ln(2)
            TableContent(
                pdf = self.pdf, 
                rows = [ [ meaning.definition_en, f"**{meaning.example}** / {meaning.example_en}" ] for meaning in word.meanings ],
                table = Table(self.pdf, line_height = int(1.35 * self.pdf.font_size), v_align = 'TOP', padding = 2, markdown = True)
            ).render()