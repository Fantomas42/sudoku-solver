"""Solvers for sudokulib"""


class BaseSolver(object):
    """BaseSolver class"""
    name = 'base solver'

    def solve(self, layer, index):
        raise NotImplementedError
