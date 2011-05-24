"""Layer for sudokulib"""
from sudokulib.constants import INDEX_REGIONS
from sudokulib.constants import REGION_INDEXES


class Layer(object):
    """Class layer for abstracting and manipulating Grid"""
    allowed_regions = ('row', 'col', 'block')

    def __init__(self, data_str, solution_str, mystery_char='X',
                 all_candidates='123456789'):
        self.mystery_char = mystery_char
        self.all_candidates = set(all_candidates)
        self.all_chars = self.all_candidates | set(self.mystery_char)

        self.table = []
        for i in range(len(data_str)):
            if not solution_str[i] in (self.mystery_char, ' '):
                self.table.append(solution_str[i])
            else:
                self.table.append(data_str[i])

    def get_region_index(self, region, index):
        """Return the table index of a region from a grid index"""
        return INDEX_REGIONS[index][region]

    def get_region(self, region, index):
        """Return the elements of a region from a grid index"""
        return [self.table[i] for i in REGION_INDEXES[region][
            self.get_region_index(region, index)]]

    def get_region_missing_indexes(self, region, index):
        """Return the missing elements's indexes
        of a region from a grid index"""
        return [i for i in
                REGION_INDEXES[region][self.get_region_index(region, index)]
                if self.table[i] == self.mystery_char and i != index]

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
        return ''.join(self.table)
