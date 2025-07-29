from fpdf import FPDF

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
    