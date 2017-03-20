"""Solver for sudokulib"""
import logging

from sudokulib.backtracking import BacktrackingSolver
from sudokulib.constants import GRID_TOTAL
from sudokulib.grid import FileSystemGrid
from sudokulib.preprocessors.block_block import BlockBlockPreprocessor
from sudokulib.preprocessors.line_block import LineBlockPreprocessor
from sudokulib.preprocessors.naked_subset import NakedSubsetPreprocessor
from sudokulib.solvers.hidden_singleton import HiddenSingletonSolver
from sudokulib.solvers.naked_singleton import NakedSingletonSolver

logger = logging.getLogger(__name__)


class SudokuSolver(object):
    """Solver of Sudoku Puzzles"""

    def __init__(self, filename, free_char='.',
                 grid_class=FileSystemGrid,
                 backtracking_solver_class=BacktrackingSolver,
                 preprocessors=[LineBlockPreprocessor,
                                BlockBlockPreprocessor,
                                NakedSubsetPreprocessor],
                 solvers=[NakedSingletonSolver,
                          HiddenSingletonSolver]):
        self.backtracking_solver_class = backtracking_solver_class
        self.solvers = solvers
        self.preprocessors = preprocessors
        self.free_char = free_char
        self.grid = grid_class(filename, self.free_char)
        self.grid.validate()

    def run(self):
        """Launch the loop of processing"""
        while not self.grid.completed:
            logger.info('%s items missing' % self.grid.missing)
            logger.info(self.__str__())

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
                i = 0
                layer = new_layer
            else:
                i += 1

        # TODO: Try to apply multiple solvers in one time
        for solver_class in self.solvers:
            for i in missing_indexes:
                solution = solver_class().solve(layer, i)
                if solution:
                    solutions.append((i, solution))
            if solutions:
                return solutions

        if self.backtracking_solver_class:
            logger.info('Sorry, but I am actually too dumb to solve '
                        'this grid, I will use a BackTracking method.')
            return self.backtracking_solver_class(
                self.preprocessors).solve(layer)

        return solutions

    def __str__(self):
        return self.grid.__str__()
