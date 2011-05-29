"""Solver for sudokulib"""
from sudokulib.grid import Grid
from sudokulib.constants import GRID_TOTAL
from sudokulib.solvers import NakedSingletonSolver
from sudokulib.solvers import HiddenSingletonSolver

from sudokulib.preprocessors import LineBlockPreprocessor
from sudokulib.preprocessors import BlockBlockPreprocessor


class SudokuSolver(object):
    """Solver of Sudoku Puzzles"""

    def __init__(self, filename, free_char='.',
                 preprocessors=[LineBlockPreprocessor,
                                BlockBlockPreprocessor],
                 solvers=[NakedSingletonSolver,
                          HiddenSingletonSolver]):
        self.solvers = solvers
        self.preprocessors = preprocessors
        self.free_char = free_char
        self.grid = Grid(filename, self.free_char)

    def run(self, verbosity):
        """Launch the loop of processing"""
        while not self.grid.completed:
            if verbosity == 2:
                print self
                print '%s items missing' % self.grid.missing

            solutions = self.process(verbosity)

            if solutions:
                self.grid.apply_solutions(solutions)
            else:
                break

    def process(self, verbosity):
        """Process the missing elements into the solvers"""
        solutions = []
        layer = self.grid.layer

        i = 0
        while i != len(self.preprocessors):
            new_layer = self.preprocessors[i]().preprocess(layer)
            if new_layer:
                if verbosity == 2:
                    print '%s has optimized the layer' % \
                          self.preprocessors[i].name
                i = 0
                layer = new_layer
            else:
                i += 1

        for solver_class in self.solvers:
            for i in range(GRID_TOTAL):
                if self.grid.data_solution[i] == self.grid.mystery_char:
                    solution = solver_class().solve(layer, i)
                    if solution:
                        solutions.append((i, solution))
                        if verbosity == 2:
                            print '%s has found %s at %s' % (
                                solver_class.name, solution, i)
            if solutions:
                return solutions
        return solutions

    def __str__(self):
        return self.grid.__str__()
