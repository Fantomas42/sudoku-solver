"""Grid for sudokulib"""
import string

from sudokulib.layer import Layer
from sudokulib.constants import GRID_TOTAL
from sudokulib.constants import GRID_WIDTH
from sudokulib.constants import BLOCK_WIDTH


class InvalidGrid(ValueError):
    pass


class BaseGrid(object):
    """Base Grid of Sudoku"""

    def __init__(self, filename, free_char='.', mystery_char='X'):
        self.filename = filename
        self.free_char = free_char
        self.mystery_char = mystery_char

        self.data = self.load_source()

        self.data_solution = ''
        for c in self.data:
            if c == self.mystery_char:
                self.data_solution += self.mystery_char
            else:
                self.data_solution += ' '

    def validate(self):
        if len(self.data) != GRID_TOTAL:
            raise InvalidGrid(u'The grid has an invalid size')

        if GRID_TOTAL - self.missing < 17:
            raise InvalidGrid(u'Not enough clues to solve the grid')

        v = [(k, c) for y in range(GRID_WIDTH)
             for x, c in enumerate(
                 self.data[y * GRID_WIDTH:(y + 1) * GRID_WIDTH])
             for k in x, y + GRID_WIDTH, (x / BLOCK_WIDTH, y / BLOCK_WIDTH)
             if c != self.mystery_char]
        if len(v) > len(set(v)):
            raise InvalidGrid(u'The grid is not a valid puzzle')

    def load_source(self):
        raise NotImplementedError

    @property
    def missing(self):
        return self.data_solution.count(self.mystery_char)

    @property
    def completed(self):
        return not self.mystery_char in self.data_solution

    @property
    def layer(self):
        return Layer(self.data, self.data_solution,
                     self.mystery_char)

    def __len__(self):
        return len(self.data)

    def apply_solutions(self, solutions):
        """Apply a solution in the solution data"""
        solution_list = list(self.data_solution)
        for index, solution in solutions:
            solution_list[index] = str(solution)
        self.data_solution = ''.join(solution_list)

    def __str__(self):
        string = []
        i = 0
        for c in self.data:
            if i and not i % GRID_WIDTH:
                string.append('\n')
            if i and not i % (GRID_WIDTH * 3):
                string.append('---------+---------+--------\n')

            if not i % 3 and i % GRID_WIDTH:
                string.append('|')

            if c == self.mystery_char:
                if self.data_solution[i] != self.mystery_char:
                    string.append(' \033[1;32m%s\033[0m ' % \
                                  self.data_solution[i])
                else:
                    string.append(' \033[1;31m%s\033[0m ' % c)
            else:
                string.append(' %s ' % c)
            i += 1

        return ''.join(string)


class FileSystemGrid(BaseGrid):
    """Grid loaded from a file on the FileSystem"""

    def load_source(self):
        source = open(self.filename, 'r')
        source_data = source.readlines()
        source_data = ''.join([line for line in source_data
                               if not line.startswith('#')])
        source.close()

        data = ''
        for c in source_data:
            if c in string.digits + self.free_char:
                if c in ('0', self.free_char):
                    data += self.mystery_char
                else:
                    data += c
        return data


class StringGrid(BaseGrid):
    """Grid loaded from a String"""

    def load_source(self):
        return self.filename.translate(string.maketrans(
            '0%s' % self.free_char, self.mystery_char * 2))
