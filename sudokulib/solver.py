"""Solver for sudokulib"""
from sudokulib.grid import Grid
from sudokulib.constants import GRID_TOTAL
from sudokulib.backtracking import BacktrackingSolver
from sudokulib.solvers.naked_singleton import NakedSingletonSolver
from sudokulib.solvers.hidden_singleton import HiddenSingletonSolver
from sudokulib.preprocessors.line_block import LineBlockPreprocessor
from sudokulib.preprocessors.block_block import BlockBlockPreprocessor
from sudokulib.preprocessors.naked_subset import NakedSubsetPreprocessor


class SudokuSolver(object):
    """Solver of Sudoku Puzzles"""

    def __init__(self, filename, free_char='.',
                 verbosity=1, backtracking=True,
                 preprocessors=[LineBlockPreprocessor,
                                BlockBlockPreprocessor,
                                NakedSubsetPreprocessor],
                 solvers=[NakedSingletonSolver,
                          HiddenSingletonSolver]):
        self.verbosity = verbosity
        self.backtracking = backtracking
        self.solvers = solvers
        self.preprocessors = preprocessors
        self.free_char = free_char
        self.grid = Grid(filename, self.free_char)

    def run(self):
        """Launch the loop of processing"""
        while not self.grid.completed:
            if self.verbosity == 2:
                print self
                print '%s items missing' % self.grid.missing

            solutions = self.process()

            if solutions:
                self.grid.apply_solutions(solutions)
            else:
                break

    def process(self):
        """Process the missing elements into the solvers"""
        solutions = []
        layer = self.grid.layer
        mystery_char = self.grid.mystery_char
        data_solution = self.grid.data_solution
        missing_indexes = [i for i in range(GRID_TOTAL)
                           if data_solution[i] == mystery_char]

        i = 0
        while i != len(self.preprocessors):
            new_layer = self.preprocessors[i]().preprocess(layer)
            if new_layer:
                if self.verbosity == 2:
                    print '%s has optimized the layer' % \
                          self.preprocessors[i].name
                i = 0
                layer = new_layer
            else:
                i += 1

        for solver_class in self.solvers:
            for i in missing_indexes:
                solution = solver_class().solve(layer, i)
                if solution:
                    solutions.append((i, solution))
                    if self.verbosity == 2:
                        print '%s has found %s at %s' % (
                            solver_class.name, solution, i)
            if solutions:
                return solutions

        if self.backtracking:
            if self.verbosity == 2:
                print 'Sorry, but I am actually too dumb to solve ' \
                      'this grid, I will use a BackTracking method.'
            return BacktrackingSolver(self.preprocessors).solve(layer)

        return solutions

    def __str__(self):
        return self.grid.__str__()
