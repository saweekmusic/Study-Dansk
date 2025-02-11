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
pdf.cell(text='Section 1: Learning New Words')
pdf.ln(13.0)

pdf.set_font(family='helvetica-neue', style='B', size=18)
pdf.cell(text='V E R B S', center=True)
pdf.ln()

pdf.set_font(family='helvetica-neue', style='B', size=30)
pdf.cell(text='Section 2: Verb Bending')
pdf.ln()

pdf.set_font(family='helvetica-neue', style='B', size=30)
pdf.cell(text='Section 3: Noun Bending')
pdf.ln()

pdf.set_font(family='helvetica-neue', style='B', size=30)
pdf.cell(text='Section 4: Connect Matches')
pdf.ln()

pdf.set_font(family='helvetica-neue', style='B', size=30)
pdf.cell(text='Section 5: Complete the Text')
pdf.ln()

pdf.set_font(family='helvetica-neue', style='B', size=30)
pdf.cell(text='Section 6: Find the Words')
pdf.ln()

pdf.set_font(family='helvetica-neue', style='B', size=30)
pdf.cell(text='Section 7: Idioms')
pdf.ln()

pdf.set_font(family='helvetica-neue', style='B', size=30)
pdf.cell(text='Section 8: Wrtie a Letter')
pdf.ln()

pdf.set_font(family='helvetica-neue', style='B', size=30)
pdf.cell(text='Section 9: Completed Text')
pdf.ln()

pdf.output("hello.pdf")