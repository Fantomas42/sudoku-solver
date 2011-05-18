"""sudokulib"""
from sudokulib.grid import Grid


class SudokuSolver(object):
    """Solver of Sudoku Puzzles"""

    def __init__(self, filename, free_char='.'):
        self.free_char = free_char
        self.grid = Grid(filename, self.free_char)

    def __str__(self):
        return self.grid.__str__()
