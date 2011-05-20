"""sudokulib"""
from sudokulib.grid import Grid
from sudokulib.solvers import SingletonSolver
from sudokulib.solvers import NakedSingletonSolver


class SudokuSolver(object):
    """Solver of Sudoku Puzzles"""

    def __init__(self, filename, free_char='.',
                 solvers=[SingletonSolver, NakedSingletonSolver]):
        self.solvers = solvers
        self.free_char = free_char
        self.grid = Grid(filename, self.free_char)

    def run(self):
        """Launch the loop of processing"""
        while not self.grid.completed:
            #print self
            #print '%s items missing' % self.grid.missing
            position, solution = self.process()
            if solution:
                self.grid.apply_solution(position, solution)
            else:
                break

    def process(self):
        """Process the missing elements into the solvers"""
        for i in range(len(self.grid)):
            if self.grid.data_solution[i] == self.grid.mystery_char:
                for solver_class in self.solvers:
                    solution = solver_class(self.grid.layer, i).solve()
                    if solution:
                        return i, solution
        return None, None

    def __str__(self):
        return self.grid.__str__()
