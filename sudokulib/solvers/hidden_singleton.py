"""Hidden Singleton solver for sudokulib"""
from sudokulib.constants import INDEX_REGIONS
from sudokulib.constants import REGION_INDEXES
from sudokulib.solvers import BaseSolver


class HiddenSingletonSolver(BaseSolver):
    """Hidden Singleton Solver
    alias: Unique Candidate"""
    name = 'Hidden Singleton'

    def _solve(self, layer, index):
        candidates = layer._candidates[index]

        for region in layer.allowed_regions:
            region_possibilities = set()
            for neighbor_index in REGION_INDEXES[region][
                    INDEX_REGIONS[index][region]]:
                if neighbor_index != index:
                    region_possibilities |= layer._candidates[neighbor_index]

            exclusion = candidates - region_possibilities
            if len(exclusion) == 1:
                return exclusion.pop()
