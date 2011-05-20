"""Solvers for sudokulib"""


class BaseSolver(object):
    """BaseSolver class"""

    def __init__(self, layer, index):
        self.layer = layer
        self.index = index

    def solve(self):
        raise NotImplementedError


class SingletonSolver(BaseSolver):
    """Simple Singleton Solver"""

    def solve(self):
        return 2
