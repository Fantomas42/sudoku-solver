"""Backtracking for sudokulib"""
from sudokulib.layer import Layer
from sudokulib.solvers import BaseSolver
from sudokulib.constants import GRID_TOTAL


class BacktrackingSolver(BaseSolver):
    """Backtrack solver"""
    name = 'Backtracking'

    def solve(self, layer):
        solutions = []
        missing = ''.join(layer.table).count(layer.mystery_char)

        if not missing:
            return True

        candidate_index = sorted([(len(layer._candidates[i]), i)
                                  for i in range(GRID_TOTAL)
                                  if len(layer._candidates[i])])
        if missing and not candidate_index:
            return None

        best_index = candidate_index[0][1]

        for candidate in layer._candidates[best_index]:
            layer_table = layer.table[:]
            layer_table[best_index] = str(candidate)
            solution_str = ''.join(layer_table)
            new_layer = Layer(solution_str, ' ' * GRID_TOTAL)
            new_solution = self.solve(new_layer)
            if not new_solution:
                continue
            if new_solution:
                if isinstance(new_solution, list):
                    solutions = [[best_index, candidate]]
                    solutions.extend(new_solution)
                else:
                    solutions = [[best_index, candidate]]

        return solutions
