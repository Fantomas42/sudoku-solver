"""Tests for sudokulib.solvers"""
from unittest import TestCase

from sudokulib.layer import Layer
from sudokulib.solvers import BaseSolver
from sudokulib.solvers.hidden_singleton import HiddenSingletonSolver
from sudokulib.solvers.naked_singleton import NakedSingletonSolver
from sudokulib.solvers.singleton import SingletonSolver


SOLUTION = ' ' * 81


class BaseSolverTestCase(TestCase):
    """Tests for BaseSolver"""

    def test_solver(self):
        solver = BaseSolver()

        layer = Layer(SOLUTION, SOLUTION)
        self.assertRaises(NotImplementedError, solver.solve, layer, 0)


class SingletonSolverTestCase(TestCase):
    """Tests for SingletonSolver"""

    def test_solve(self):
        solver = SingletonSolver()
        # Row resolution
        data = '1234567X957813962449687215395238146764129' \
               '7835387564291719623548864915372235748916'
        layer = Layer(data, SOLUTION)
        self.assertEqual(solver.solve(layer, 7), '8')

        # Col resolution
        data = '123X56X8957813962449687215395238146764129' \
               '7835387564291719623548864915372235748916'
        layer = Layer(data, SOLUTION)
        self.assertEqual(solver.solve(layer, 3), '4')

        # Block resolution
        data = '123X56X89578139624496872153952381467641X9' \
               '7835387564291719623548864915372235X48916'
        layer = Layer(data, SOLUTION)
        self.assertEqual(solver.solve(layer, 3), '4')

        # No resolution
        data = '12345678957813962449687215395238146764129' \
               '7835387564291719623548864915372235748916'
        layer = Layer(data, SOLUTION)
        self.assertEqual(solver.solve(layer, 7), 'X')


class NakedSingletonSolverTestCase(TestCase):
    """Tests for NakedSingletonSolver"""

    def test_solve(self):
        solver = NakedSingletonSolver()
        data = '1X96X4X2X53X2XXXXXXX8XXX1X5XXXXX6X5XXXXX4' \
               'XXXXX6X3XXXXX2X1XXX7XXXXXXX5X13X8X7X95X2'
        layer = Layer(data, SOLUTION)
        self.assertEqual(solver.solve(layer, 21), '9')


class HiddenSingletonSolverTestCase(TestCase):
    """Tests for HiddenSingletonSolver"""

    def test_solve(self):
        solver = HiddenSingletonSolver()
        data = '1XXXX4X7X24X5XXXXXXXXXX3XX8XXXXXX9XX851X7' \
               'X432XX2XXXXXX3XX9XXXXXXXXXX5X93X6X8XXXX1'
        layer = Layer(data, SOLUTION)
        self.assertEqual(solver.solve(layer, 25), '4')
