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
        self.assertEquals(solver.grid.completed, False)
        solver.run()
        self.assertEquals(solver.grid.completed, True)
