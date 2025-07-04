from fpdf import FPDF

from src.Modules.Body import Body


class Section:
    def __init__(self, pdf: FPDF, title: str, description: str, body: list[Body] = []) -> None:
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
        self.pdf.ln(10)

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
        self.pdf.set_text_color(150)
        self.pdf.set_font(family='helvetica-neue', style='I', size=self.body_size)
        self.pdf.write(text=self.description)
        self.pdf.set_text_color(0)
        self.pdf.ln()

    def render_body(self):
        for body in self.body:
            self.pdf.ln(4) 
            body.render()
