# from src.Modules.PDFClass import PDF
# from src.Constants import *

# class Section():
#     '''Docstring. Not present for now.'''

#     def __init__(self) -> None:
#         self.pdf = PDF()

#         # Page settings 
#         self.pdf.set_left_margin(15)
#         self.pdf.set_auto_page_break(auto=True, margin=15)
#         self.pdf.set_right_margin(15)
#         self.pdf.set_top_margin(15)

#         # Add fonts
#         self.pdf.add_font('helvetica-neue', 
#                       style='', 
#                       fname='src/Fonts/HelveticaNeue-01.ttf',
#                       uni=True)
#         self.pdf.add_font('helvetica-neue', 
#                       style='B', 
#                       fname='src/Fonts/HelveticaNeue-Bold-02.ttf',
#                       uni=True)
#         self.pdf.add_font('helvetica-neue', 
#                       style='I', 
#                       fname='src/Fonts/HelveticaNeue-Italic-03.ttf',
#                       uni=True)
#         self.pdf.add_font('helvetica-neue', 
#                       style='BI', 
#                       fname='src/Fonts/HelveticaNeue-BoldItalic-04.ttf',
#                       uni=True)
        
#         # First page initialization
#         self.pdf.add_page()

#     def section1(self, title = 'Section 1: Learning New Words'):
#         self.pdf.print_title(title)

#         for pos in list(POS_TYPES.keys()):
#             self.pdf.print_subtitle(pos)
#             self.pdf.print_words('', '', POS_TYPES[pos])

#     def section2(self):
#         pass
    
#     def section3(self):
#         pass

#     def section4(self):
#         pass

#     def section5(self):
#         pass

#     def section6(self):
#         pass

#     def section7(self):
#         pass











# New Way
from src.Modules.Body import Body
from fpdf import FPDF

class Section:
    def __init__(self, pdf: FPDF, title: str, description: str, body: list[Body]) -> None:
        self.pdf = pdf
        self.title = title
        self.description = description
        self.body = body

        self.title_size = 30
        self.body_size = 11

    def add_body(self, body: Body):
        self.body.append(body)

    def render(self):
        self.render_title()
        self.render_description()
        self.render_body()
        # Additional rendering logic can be added here if needed

    def render_title(self):
        self.pdf.set_font(family='helvetica-neue', style='B', size=self.title_size)
        self.pdf.write(text=self.title)
        self.pdf.ln()
        self.pdf.ln(2)

        # Line under the title
        with self.pdf.local_context(line_width=0.5):
            self.pdf.set_draw_color(r=179, g=179, b=179)
            self.pdf.line(
                self.pdf.l_margin, 
                self.pdf.get_y(),
                self.pdf.w - self.pdf.r_margin,
                self.pdf.get_y())

    def render_description(self):
        self.pdf.ln(2)
        self.pdf.set_font(family='helvetica-neue', style='', size=self.body_size)
        self.pdf.write(text=self.description)

    def render_body(self):
        for body in self.body:
            body.render()
