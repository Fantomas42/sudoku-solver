"""Singleton solver for sudokulib"""
from sudokulib.solvers import BaseSolver


class SingletonSolver(BaseSolver):
    """Simple Singleton Solver (deprecated)"""
    name = 'Singleton'

    def _solve(self, layer, index):
        all_chars_length = len(layer.all_chars)

        for region in layer.allowed_regions:
            region_set = set(layer.get_region(region, index))
            if all_chars_length - len(region_set) == 1:
                return (layer.all_chars - region_set).pop()
