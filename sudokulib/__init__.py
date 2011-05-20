"""sudokulib"""
from sudokulib.grid import Grid


class SudokuSolver(object):
    """Solver of Sudoku Puzzles"""

    def __init__(self, filename, free_char='.'):
        self.free_char = free_char
        self.grid = Grid(filename, self.free_char)

    def run(self):

        while not self.grid.completed:
            layer = self.grid.layer

            position, solution = self.process(layer)
            self.grid.apply_solution(position, solution)
            self.grid.data_solution = ' ' * 81  # Provoque completed

    def process(self, layer):
        return 4, 2

    def __str__(self):
        return self.grid.__str__()
