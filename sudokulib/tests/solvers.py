"""Tests for sudokulib.solvers"""
from unittest import TestCase

from sudokulib.layer import Layer
from sudokulib.solvers import SingletonSolver

DATA_SET = '1234567X957813962449687215395238146764129' \
           '7835387564291719623548864915372235748916'
SOLUTION = '                                         ' \
           '                                        '


class SingletonSolverTestCase(TestCase):

    def setUp(self):
        self.layer = Layer(DATA_SET, SOLUTION)

    def test_solve(self):
        solver = SingletonSolver(self.layer, 7)
        self.assertEquals(solver.solve(), '8')
