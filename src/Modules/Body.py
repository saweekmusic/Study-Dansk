from src.Modules.PDFClass import PDF
from src.Constants import *

class Body:
    def render(self):
        raise NotImplementedError("Subclasses should implement this method")
    
class WordContent(Body):
    pass

class TableContent(Body):
    pass

class TextContent(Body):
    def __init__(self, pdf: PDF, text: str) -> None:
        self.pdf = pdf
        self.text = text

    def render(self):
        self.pdf.set_font(family='helvetica-neue', style='', size=BODY_SIZE)
        self.pdf.write(text=self.text)