"""Solvers for sudokulib"""


class BaseSolver(object):
    """BaseSolver class"""
    name = 'base solver'

    def solve(self, layer, index):
        raise NotImplementedError


class SingletonSolver(BaseSolver):
    """Simple Singleton Solver (deprecated)"""
    name = 'Singleton'

    def solve(self, layer, index):
        all_chars_length = len(layer.all_chars)

        for region in layer.allowed_regions:
            region_set = set(layer.get_region(region, index))
            if all_chars_length - len(region_set) == 1:
                return (layer.all_chars - region_set).pop()

        return None


class NakedSingletonSolver(BaseSolver):
    """Naked Singleton Solver
    alias: Sole Candidate"""
    name = 'Naked Singleton'

    def solve(self, layer, index):
        candidates = layer._candidates[index]
        if len(candidates) == 1:
            return candidates.pop()

        return None


class HiddenSingletonSolver(BaseSolver):
    """Hidden Singleton Solver
    alias: Unique Candidate"""
    name = 'Hidden Singleton'

    def solve(self, layer, index):
        candidates = layer._candidates[index]

        for region in layer.allowed_regions:
            region_possibilities = set()
            for index_missing in layer.get_region_missing_indexes(
                region, index):
                region_possibilities |= layer._candidates[index_missing]

            exclusion = candidates - region_possibilities
            if len(exclusion) == 1:
                return exclusion.pop()

        return None
