import math

from fpdf import FPDF
from fpdf.table import Table

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

def table_height(pdf: FPDF, table: Table):
    # Ensure column count
    table._cols_count = max(row.cols_count for row in table.rows) if table.rows else 0

    # Ensure width is set
    if table._width is None:
        if table._col_widths and isinstance(table._col_widths, (int, float)):
            table._width = table._cols_count * table._col_widths
        else:
            table._width = table._fpdf.epw  # effective page width

    # Set outer margins if they aren't set yet
    if not hasattr(table, '_outer_border_margin') or table._outer_border_margin is None:
        if table._outer_border_width:
            table._outer_border_margin = (
                table._gutter_width + table._outer_border_width / 2,
                table._gutter_height + table._outer_border_width / 2,
            )
        else:
            table._outer_border_margin = (0, 0)

    # Get row info and sum heights
    row_infos = list(table._compute_rows_info())
    if not row_infos:
        return 0

    total_height = sum(info.height for info in row_infos)
    total_height += table._gutter_height * (len(row_infos) - 1)
    total_height += 2 * table._outer_border_margin[1]

    return math.ceil(total_height)