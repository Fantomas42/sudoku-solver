"""Backtracking for sudokulib"""
from sudokulib.constants import GRID_TOTAL
from sudokulib.layer import Layer

VOID_SOLUTION = ' ' * GRID_TOTAL


class BacktrackingSolver(object):
    """Backtrack solver"""
    name = 'Backtracking'

    def __init__(self, preprocessors=[]):
        """Simply register the preprocessors
        to use at the initialization"""
        self.preprocessors = preprocessors

    def preprocess(self, layer):
        """Apply the preprocessors on the layer"""
        i = 0
        while i != len(self.preprocessors):
            new_layer = self.preprocessors[i]().preprocess(layer)
            if new_layer:
                layer = new_layer
                i = 0
            else:
                i += 1
        return layer

    def solve(self, layer):
        """Apply a backtracking algorithm with preprocessors
        optimizations to reduce possibilities to compute"""
        layer = self.preprocess(layer)

        solutions = []
        missings_str = ''.join(layer.table)
        missings = missings_str.count(layer.mystery_char)

        if missings == 1:
            missing_index = missings_str.index(layer.mystery_char)
            missing_candidates = layer._candidates[missing_index]
            return [[missing_index, missing_candidates.pop()]]

        candidate_indexes = []
        for i in range(GRID_TOTAL):
            candidates = layer._candidates[i]
            if candidates:
                candidate_indexes.append((len(candidates), i))

        if not candidate_indexes:
            return None

        best_index = sorted(candidate_indexes)[0][1]

        for candidate in layer._candidates[best_index]:
            layer_table = layer.table[:]
            layer_table[best_index] = str(candidate)
            solution_str = ''.join(layer_table)
            new_layer = Layer(solution_str, VOID_SOLUTION)
            new_solution = self.solve(new_layer)
            if not new_solution:
                continue
            else:
                solutions = [[best_index, candidate]]
                solutions.extend(new_solution)

        return solutions
