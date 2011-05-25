"""Solvers for sudokulib"""


class BaseSolver(object):
    """BaseSolver class"""
    name = 'base solver'

    def solve(self, layer, index):
        raise NotImplementedError


class SingletonSolver(BaseSolver):
    """Simple Singleton Solver"""
    name = 'Singleton'

    def solve(self, layer, index):
        for region in layer.allowed_regions:
            region_set = set(layer.get_region(region, index))
            if len(layer.all_chars) - len(region_set) == 1:
                return (layer.all_chars - region_set).pop()

        return None


class NakedSingletonSolver(BaseSolver):
    """Naked Singleton Solver"""
    name = 'Naked Singleton'

    def solve(self, layer, index):
        excluded = layer.get_excluded(index)

        if len(layer.all_chars) - len(excluded) == 1:
            return (layer.all_chars - excluded).pop()

        return None


class HiddenSingletonSolver(BaseSolver):
    """Hidden Singleton Solver"""
    name = 'Hidden Singleton'

    def solve(self, layer, index):
        candidates = layer.get_candidates(index)

        for region in layer.allowed_regions:
            region_possibilities = set()
            for index_missing in layer.get_region_missing_indexes(
                region, index):
                region_possibilities |= layer.get_candidates(index_missing)

            exclusion = candidates - region_possibilities
            if len(exclusion) == 1:
                return exclusion.pop()

        return None
