"""Layer for sudokulib"""
from sudokulib.constants import GRID_WIDTH
from sudokulib.constants import BLOCK_WIDTH


class Layer(object):
    """Class layer for abstracting and manipulating Grid"""

    def __init__(self, data_str, solution_str, mystery_char='X'):
        self.str = ''
        for i in range(len(data_str)):
            if not solution_str[i] in (mystery_char, ' '):
                self.str += solution_str[i]
            else:
                self.str += data_str[i]

        self.col_table = []
        self.row_table = []
        self.block_table = []
        for i in range(GRID_WIDTH):
            offset = i * GRID_WIDTH
            self.col_table.append(list(self.str[i::GRID_WIDTH]))
            self.row_table.append(list(self.str[offset:offset + GRID_WIDTH]))

            block = ''
            block_offset = ((i / BLOCK_WIDTH) * GRID_WIDTH * BLOCK_WIDTH) + \
                           ((i % BLOCK_WIDTH) * BLOCK_WIDTH)
            for j in range(BLOCK_WIDTH):
                block += self.str[block_offset:block_offset + BLOCK_WIDTH]
                block_offset += GRID_WIDTH
            self.block_table.append(list(block))

    def __str__(self):
        return self.str
