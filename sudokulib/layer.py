"""Layer for sudokulib"""
from sudokulib.constants import GRID_TOTAL
from sudokulib.constants import GRID_WIDTH
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
        # Assignate elems in table
        for i in range(GRID_TOTAL):
            if not solution_str[i] in (self.mystery_char, ' '):
                self.table.append(solution_str[i])
            else:
                self.table.append(data_str[i])

        self.region_table = {'col': [], 'row': [], 'block': []}
        # Assignate shortcut tables
        for i in range(GRID_WIDTH):
            self.region_table['row'].append([
                self.table[j] for j in REGION_INDEXES['row'][i]])
            self.region_table['col'].append([
                self.table[j] for j in REGION_INDEXES['col'][i]])
            self.region_table['block'].append([
                self.table[j] for j in REGION_INDEXES['block'][i]])

        self._excluded = {}
        self._candidates = {}
        # Assignate candidates and excluded
        for i in range(GRID_TOTAL):
            if self.table[i] == self.mystery_char:
                ir = INDEX_REGIONS[i]
                excluded = (set(self.region_table['row'][ir['row']])
                            | set(self.region_table['col'][ir['col']])
                            | set(self.region_table['block'][ir['block']]))
                self._excluded[i] = excluded
                self._candidates[i] = self.all_chars - excluded
            else:
                self._excluded[i] = set()
                self._candidates[i] = set()

    def get_region_index(self, region, index):
        """Return the table index of a region from a grid index"""
        return INDEX_REGIONS[index][region]

    def get_region(self, region, index):
        """Return the elements of a region from a grid index"""
        return self.region_table[region][
            INDEX_REGIONS[index][region]]

    def get_region_missing_indexes(self, region, index):
        """Return the missing elements's indexes"""
        return [i for i in
                REGION_INDEXES[region][INDEX_REGIONS[index][region]]
                if self.table[i] == self.mystery_char and i != index]

    def get_excluded(self, index):
        """Return a set of solution for an index"""
        return self._excluded[index]

    def get_candidates(self, index):
        """Return a set of candidates for an index"""
        return self._candidates[index]

    def __str__(self):
        return ''.join(self.table)
