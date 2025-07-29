from fpdf.enums import CellBordersLayout
from fpdf.enums import Align
from fpdf.enums import VAlign, Align
from fpdf import FontFace
from typing import Optional, Union

class TableCell:
    def __init__(
            self, 
            text: str = '', 
            align: Optional[Union[str, Align]] = None, 
            v_align: Optional[Union[str, VAlign]] = None, 
            style: Optional[FontFace] = None, 
            img: Optional[str] = None, 
            img_fill_width: bool = False, 
            colspan: int = 1, 
            rowspan: int = 1, 
            padding: tuple[float, ...] | None = None, 
            link: Optional[Union[str, int]] = None, 
            border: CellBordersLayout | int | str = CellBordersLayout.INHERIT):
        self.text = text
        self.align = align
        self.v_align = v_align
        self.style = style
        self.img = img
        self.img_fill_width = img_fill_width
        self.colspan = colspan
        self.rowspan = rowspan
        self.padding = padding
        self.link = link
        self.border = border if isinstance(border, (int, CellBordersLayout)) else CellBordersLayout.coerce(border)