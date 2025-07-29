from fpdf import FPDF

def calculate_text_height(pdf: FPDF, text: str, font_size: int, width: float | None = None) -> int:
    if width is None:
        width = pdf.epw

    if font_size <= 0:
        raise ValueError('Font size must be greater than 0')
    
    original_font_size = int(pdf.font_size)
    pdf.set_font(size = font_size)

    # Line height based on font size
    line_height = font_size * 0.352777778  # pt to mm

    # Wrap manually
    words = text.split()
    lines = []
    current_line = ''

    for word in words:
        test_line = (current_line + ' ' + word).strip()

        if pdf.get_string_width(test_line) <= width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
            
    if current_line:
        lines.append(current_line)
    
    # Restore original font size if it was changed
    pdf.set_font(size = original_font_size)

    return int(line_height * len(lines))