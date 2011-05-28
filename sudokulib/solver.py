"""Solver for sudokulib"""
from sudokulib.grid import Grid
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

            position, solution = self.process(verbosity)

            if solution:
                self.grid.apply_solution(position, solution)
            else:
                break

    def process(self, verbosity):
        """Process the missing elements into the solvers"""
        layer = self.grid.layer

        i = 0
        while i != len(self.preprocessors):
            new_layer = self.preprocessors[i]().preprocess(layer)
            if new_layer:
                i = 0
                layer = new_layer
                if verbosity == 2:
                    print '%s has optimized the layer' % \
                          self.preprocessors[i].name
            else:
                i += 1

        for i in range(len(self.grid)):
            if self.grid.data_solution[i] == self.grid.mystery_char:
                for solver_class in self.solvers:
                    solution = solver_class().solve(layer, i)
                    if solution:
                        if verbosity == 2:
                            print '%s has found %s at %s' % (
                                solver_class.name, solution, i)
                        return i, solution
        return None, None

    def __str__(self):
        return self.grid.__str__()
