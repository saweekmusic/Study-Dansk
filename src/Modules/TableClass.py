from fpdf.table import Table

class CustomTable(Table):
    def get_total_height(self):
        """
        Estimate total table height (with padding, gutters, and spans), without rendering.
        """
        # Ensure column count
        self._cols_count = max(row.cols_count for row in self.rows) if self.rows else 0

        # Ensure width is set
        if self._width is None:
            if self._col_widths and isinstance(self._col_widths, (int, float)):
                self._width = self._cols_count * self._col_widths
            else:
                self._width = self._fpdf.epw  # effective page width

        # Set outer margins if they aren't set yet
        if not hasattr(self, "_outer_border_margin") or self._outer_border_margin is None:
            if self._outer_border_width:
                self._outer_border_margin = (
                    self._gutter_width + self._outer_border_width / 2,
                    self._gutter_height + self._outer_border_width / 2,
                )
            else:
                self._outer_border_margin = (0, 0)

        # Get row info and sum heights
        row_infos = list(self._compute_rows_info())
        if not row_infos:
            return 0

        total_height = sum(info.height for info in row_infos)
        total_height += self._gutter_height * (len(row_infos) - 1)
        total_height += 2 * self._outer_border_margin[1]

        return total_height