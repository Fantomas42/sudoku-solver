"""Tests for sudokulib.solver"""
from unittest import TestCase

from sudokulib.grid import StringGrid
from sudokulib.solver import SudokuSolver


class SudokuSolverTestCase(TestCase):
    """Tests for SudokuSolver"""

    def test_solve(self):
        grid = '1638.5.7...8.4..65..5..7..845..82.393.1..' \
               '..4.7........839.5....6.42..59.....93.81'
        solver = SudokuSolver(grid, grid_class=StringGrid)
        self.assertEqual(solver.grid.completed, False)
        solver.run()
        self.assertEqual(solver.grid.completed, True)

    def test_unsolvable_without_backtracking(self):
        grid = '.5.9.7.4.1..8.2..5.7..1..3...4...8..72...' \
               '..16..1...2...9..8..2.2..6.9..1.1.7.3.8.'
        solver = SudokuSolver(grid, grid_class=StringGrid,
                              backtracking_solver_class=None)
        self.assertEqual(solver.grid.completed, False)
        solver.run()
        self.assertEqual(solver.grid.completed, False)

    def test_use_backtracking(self):
        grid = '123456.8957813962449687215395238146764129' \
               '7835387564291719623548864915372235748916'
        solver = SudokuSolver(grid, grid_class=StringGrid,
                              solvers=[])
        self.assertEqual(solver.grid.completed, False)
        solver.run()
        self.assertEqual(solver.grid.completed, True)
