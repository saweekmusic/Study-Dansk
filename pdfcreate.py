from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

pdf.add_font('helvetica-neue', style='', fname='Fonts/HelveticaNeue-01.ttf')
pdf.add_font('helvetica-neue', style='B', fname='Fonts/HelveticaNeue-Bold-02.ttf')
pdf.add_font('helvetica-neue', style='I', fname='Fonts/HelveticaNeue-Italic-03.ttf')
pdf.add_font('helvetica-neue', style='BI', fname='Fonts/HelveticaNeue-BoldItalic-04.ttf')
pdf.add_font('helvetica-neue-light', style='', fname='Fonts/HelveticaNeue-01.ttf')
pdf.add_font('helvetica-neue-light', style='I', fname='Fonts/HelveticaNeue-01.ttf')
pdf.set_font(family='helvetica-neue', style='B', size=30)

pdf.cell(text='Section 1: HELLO')
pdf.output("hello.pdf")