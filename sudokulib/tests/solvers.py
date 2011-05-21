"""Tests for sudokulib.solvers"""
from unittest import TestCase

from sudokulib.layer import Layer
from sudokulib.solvers import SingletonSolver
from sudokulib.solvers import NakedSingletonSolver


SOLUTION = '                                         ' \
           '                                        '


class SingletonSolverTestCase(TestCase):
    """Tests for SingletonSolver"""

    def test_solve(self):
        # Row resolution
        data = '1234567X957813962449687215395238146764129' \
               '7835387564291719623548864915372235748916'
        layer = Layer(data, SOLUTION)
        solver = SingletonSolver(layer, 7)
        self.assertEquals(solver.solve(), '8')

        # Col resolution
        data = '123X56X8957813962449687215395238146764129' \
               '7835387564291719623548864915372235748916'
        layer = Layer(data, SOLUTION)
        solver = SingletonSolver(layer, 3)
        self.assertEquals(solver.solve(), '4')

        # Blokc resolution
        data = '123X56X89578139624496872153952381467641X9' \
               '7835387564291719623548864915372235748916'
        layer = Layer(data, SOLUTION)
        solver = SingletonSolver(layer, 3)
        self.assertEquals(solver.solve(), '4')


class NakedSingletonSolverTestCase(TestCase):
    """Tests for NakedSingletonSolver"""

    def test_solve(self):
        data = '1X96X4X2X53X2XXXXXXX8XXX1X5XXXXX6X5XXXXX4' \
               'XXXXX6X3XXXXX2X1XXX7XXXXXXX5X13X8X7X95X2'
        layer = Layer(data, SOLUTION)
        solver = NakedSingletonSolver(layer, 21)
        self.assertEquals(solver.solve(), '9')
