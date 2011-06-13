"""Naked Singleton solver for sudokulib"""
from sudokulib.solvers import BaseSolver


class NakedSingletonSolver(BaseSolver):
    """Naked Singleton Solver
    alias: Sole Candidate"""
    name = 'Naked Singleton'

    def _solve(self, layer, index):
        candidates = layer._candidates[index]
        if len(candidates) == 1:
            return candidates.pop()
