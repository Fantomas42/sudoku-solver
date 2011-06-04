"""Backtracking for sudokulib"""
from sudokulib.layer import Layer
from sudokulib.solvers import BaseSolver
from sudokulib.constants import GRID_TOTAL

VOID_SOLUTION = ' ' * GRID_TOTAL


class BacktrackingSolver(BaseSolver):
    """Backtrack solver"""
    name = 'Backtracking'

    def solve(self, layer):
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
