"""Grid for sudokulib"""
import string
try:
    from string import maketrans
except ImportError:  # Python 3
    maketrans = str.maketrans

from sudokulib.constants import BLOCK_WIDTH
from sudokulib.constants import GRID_TOTAL
from sudokulib.constants import GRID_WIDTH
from sudokulib.layer import Layer

INVALID_GRID_SIZE = u'The grid has an invalid size.'
INVALID_GRID_CLUES = u'Not enough clues to solve the grid.'
INVALID_GRID_PUZZLE = u'The grid is not a valid puzzle.'


class InvalidGrid(ValueError):
    """Exception raised when a Grid instance
    is not valid"""
    pass


class BaseGrid(object):
    """Base Grid of Sudoku"""

    def __init__(self, filename, free_char='.', mystery_char='X'):
        """Initialize the grid attributes,
        load the grid and prepare the solution"""
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
        """Validate the grid as a valid puzzle by :
         * checking the size
         * check the number of clues
         * check blocking solutions"""
        if len(self) != GRID_TOTAL:
            raise InvalidGrid(INVALID_GRID_SIZE)

        if GRID_TOTAL - self.missing < 17:
            raise InvalidGrid(INVALID_GRID_CLUES)

        v = []
        for y in range(GRID_WIDTH):
            for x, c in enumerate(
                    self.data[y * GRID_WIDTH:(y + 1) * GRID_WIDTH]):
                for k in x, y + GRID_WIDTH, (x / BLOCK_WIDTH, y / BLOCK_WIDTH):
                    if c != self.mystery_char:
                        v.append((k, c))
        if len(v) > len(set(v)):
            raise InvalidGrid(INVALID_GRID_PUZZLE)

        return True

    def load_source(self):
        raise NotImplementedError

    @property
    def missing(self):
        """Return the number of remaining
        missing items in the grid"""
        return self.data_solution.count(self.mystery_char)

    @property
    def completed(self):
        """Check if the grid is completed"""
        return self.mystery_char not in self.data_solution

    @property
    def layer(self):
        """Return a Layer instance based on
        the current state of the grid"""
        return Layer(self.data, self.data_solution,
                     self.mystery_char)

    def apply_solutions(self, solutions):
        """Apply a multiple solution on the grid"""
        solution_list = list(self.data_solution)
        for index, solution in solutions:
            solution_list[index] = str(solution)
        self.data_solution = ''.join(solution_list)

    def __len__(self):
        return len(self.data)

    def __str__(self):
        grid_string = []
        i = 0
        for c in self.data:
            if i and not i % GRID_WIDTH:
                grid_string.append('\n')
            if i and not i % (GRID_WIDTH * 3):
                grid_string.append('---------+---------+--------\n')

            if not i % 3 and i % GRID_WIDTH:
                grid_string.append('|')

            if c == self.mystery_char:
                if self.data_solution[i] != self.mystery_char:
                    grid_string.append(' \033[1;32m%s\033[0m ' %
                                       self.data_solution[i])
                else:
                    grid_string.append(' \033[1;31m%s\033[0m ' % c)
            else:
                grid_string.append(' %s ' % c)
            i += 1

        return ''.join(grid_string)


class FileSystemGrid(BaseGrid):
    """Grid loaded from a file located on the FileSystem"""

    def load_source(self):
        """Load a grid from a file on the FileSystem
        escaping lines starting by '#' and characters
        not in r'[%s0-9]' % self.free_char"""
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
        """Load a grid based on self.filename and consider
        '0' + self.free_char as a missing item in the grid"""
        return self.filename.translate(maketrans(
            '0%s' % self.free_char, self.mystery_char * 2))
