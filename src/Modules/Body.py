from src.Modules.PDFClass import PDF
from fpdf.table import Table
from Functions.Calculate import table_height
from src.Constants import BODY_SIZE
from fpdf.enums import Align

class Body:
    def render(self):
        raise NotImplementedError("Subclasses should implement this method")
    
class WordContent(Body):
    pass

class TableContent(Body):
    def __init__(self, pdf: PDF, rows: list[list[str]], table: Table, square: bool = False) -> None:
        self.pdf = pdf
        self.rows = rows
        self.table = table
        # self.width = pdf.epw

        # Setting the table
        for row in rows:
            self.table.row(row)

        if square:
            self.table._width = table_height(self.pdf, self.table) # type: ignore
            self.table._text_align = Align.coerce('C') # type: ignore

    def render(self):
        self.pdf.set_font(family='helvetica', style='', size=BODY_SIZE)
        self.table.render()

class TextContent(Body):
    def __init__(self, pdf: PDF, text: str) -> None:
        self.pdf = pdf
        self.text = text

    def render(self):
        self.pdf.set_font(family='helvetica-neue', style='', size=BODY_SIZE)
        self.pdf.write(text=self.text)