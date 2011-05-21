"""Layer for sudokulib"""
from sudokulib.constants import GRID_WIDTH
from sudokulib.constants import BLOCK_WIDTH


class Layer(object):
    """Class layer for abstracting and manipulating Grid"""
    allowed_regions = ('row', 'col', 'block')

    def __init__(self, data_str, solution_str, mystery_char='X'):
        self.mystery_char = mystery_char
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

    def get_region_index(self, region, index):
        if not region in self.allowed_regions:
            raise ValueError('Invalid region name')
        if region == 'row':
            return index / GRID_WIDTH
        elif region == 'col':
            return index % GRID_WIDTH
        return ((index / (BLOCK_WIDTH * GRID_WIDTH) * BLOCK_WIDTH) + \
                ((index % (BLOCK_WIDTH * GRID_WIDTH) / BLOCK_WIDTH) %
                 BLOCK_WIDTH))

    def get_region(self, region, index):
        index = self.get_region_index(region, index)
        return getattr(self, '%s_table' % region)[index]

    def __str__(self):
        return self.str
