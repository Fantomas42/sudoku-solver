"""sudokulib"""


class Grid(object):
    """Grid of Sudoku"""

    def __init__(self, filename):
        self.filename = filename
        source = open(filename, 'r')
        self.data = source.readlines()
        source.close()

        self.height = len(self.data)
        self.width = len(self.data[0])
        self.check_source()

    def check_source(self):
        for line in self.data:
            if self.width != len(line):
                print u'Invalid source file'
                exit(1)

    def __str__(self):
        return '\n'.join(self.data)


class SudokuSolver(object):
    """Solver of Sudoku Puzzles"""

    def __init__(self, filename, free_char='.'):
        self.free_char = free_char
        self.grid = Grid(filename)

    def __str__(self):
        return self.grid.__str__()
