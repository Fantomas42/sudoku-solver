"""Layer for sudokulib"""
from sudokulib.constants import GRID_WIDTH
from sudokulib.constants import BLOCK_WIDTH


class Layer(object):
    """Class layer for abstracting and manipulating Grid"""
    allowed_regions = ('row', 'col', 'block')

    def __init__(self, data_str, solution_str, mystery_char='X',
                 all_candidates='123456789'):
        self.mystery_char = mystery_char
        self.all_candidates = set(all_candidates)
        self.all_chars = self.all_candidates | set(self.mystery_char)

        self.str = ''
        for i in range(len(data_str)):
            if not solution_str[i] in (self.mystery_char, ' '):
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
        """Return the table index of a region from a grid index"""
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
        """Return the elements of a region from a grid index"""
        index = self.get_region_index(region, index)
        return getattr(self, '%s_table' % region)[index]

    def get_region_missing_indexes(self, region, index):
        """Return the missing elements's indexes
        of a region from a grid index"""
        missing_indexes = []
        region = self.get_region(region, index)
        # TODO
        return missing_indexes

    def get_excluded(self, index):
        """Return a set of solution for an index"""
        all_regions_set = set()
        for region in self.allowed_regions:
            all_regions_set |= set(self.get_region(region, index))
        return all_regions_set

    def get_candidates(self, index):
        """Return a set of candidates for an index"""
        return self.all_chars - self.get_excluded(index)

    def __str__(self):
        return self.str
