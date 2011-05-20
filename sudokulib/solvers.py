"""Solvers for sudokulib"""


class BaseSolver(object):
    """BaseSolver class"""

    def __init__(self, layer, index):
        self.layer = layer
        self.index = index
        self.exclude_set = set('123456789' + self.layer.mystery_char)

    def solve(self):
        raise NotImplementedError


class SingletonSolver(BaseSolver):
    """Simple Singleton Solver"""

    def solve(self):
        row_set = set(self.layer.get_row(self.index))
        if len(row_set) == 9 and self.layer.mystery_char in row_set:
            return (self.exclude_set - row_set).pop()

        col_set = set(self.layer.get_col(self.index))
        if len(col_set) == 9 and self.layer.mystery_char in col_set:
            return (self.exclude_set - col_set).pop()

        block_set = set(self.layer.get_block(self.index))
        if len(block_set) == 9 and self.layer.mystery_char in block_set:
            return (self.exclude_set - block_set).pop()

        return None


class NakedSingletonSolver(BaseSolver):
    """Naked Singleton Solver"""

    def solve(self):
        all_set = set(self.layer.get_row(self.index)) | \
                  set(self.layer.get_col(self.index)) | \
                  set(self.layer.get_block(self.index))
        if len(all_set) == 9 and self.layer.mystery_char in all_set:
            return (self.exclude_set - all_set).pop()
