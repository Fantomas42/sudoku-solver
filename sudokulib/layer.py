"""Layer for sudokulib"""
from sudokulib.constants import GRID_WIDTH


class Layer(object):
    """Class layer for abstracting and manipulating Grid"""

    def __init__(self, data_str, solution_str, mystery_char='X'):
        self.str = ''
        for i in range(len(data_str)):
            if not solution_str[i] in (mystery_char, ' '):
                self.str += solution_str[i]
            else:
                self.str += data_str[i]

        self.row_table = []
        for i in range(GRID_WIDTH):
            self.row_table.append(list(self.str[i:i + GRID_WIDTH]))

    def __str__(self):
        return self.str
