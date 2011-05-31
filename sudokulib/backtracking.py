"""Backtracking for sudokulib"""
from sudokulib.solvers import BaseSolver


class BacktrackSolver(BaseSolver):
    """Backtrack solver"""
    name = 'Backtracking'

    def solver(self, laver, index):
        pass
