"""Solvers for sudokulib"""


class BaseSolver(object):
    """BaseSolver class"""
    name = 'base solver'

    def __init__(self, layer, index):
        self.layer = layer
        self.index = index

    def solve(self):
        raise NotImplementedError


class SingletonSolver(BaseSolver):
    """Simple Singleton Solver"""
    name = 'Singleton'

    def solve(self):
        for region in self.layer.allowed_regions:
            region_set = set(self.layer.get_region(region, self.index))
            if len(self.layer.all_chars) - len(region_set) == 1:
                return (self.layer.all_chars - region_set).pop()

        return None


class NakedSingletonSolver(BaseSolver):
    """Naked Singleton Solver"""
    name = 'Naked Singleton'

    def solve(self):
        excluded = self.layer.get_excluded(self.index)

        if len(self.layer.all_chars) - len(excluded) == 1:
            return (self.layer.all_chars - excluded).pop()

        return None


class HiddenSingletonSolver(BaseSolver):
    """Hidden Singleton Solver"""
    name = 'Hidden Singleton'

    def solve(self):
        for region in self.layer.allowed_regions:
            region_possibilities = set()
            for index_missing in self.layer.get_region_missing_indexes(
                region, self.index):
                region_possibilities |= self.layer.get_candidates(
                    index_missing)

            exclusion = self.layer.get_candidates(self.index) - \
                        region_possibilities
            if len(exclusion) == 1:
                return exclusion.pop()

        return None
