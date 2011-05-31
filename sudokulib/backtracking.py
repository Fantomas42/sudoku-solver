"""Backtracking for sudokulib"""
from sudokulib.solvers import BaseSolver


class BacktrackingSolver(BaseSolver):
    """Backtrack solver"""
    name = 'Backtracking'

    def solve(self, layer):
        return ()
