"""Tests for sudokulib.backtracking"""
from unittest import TestCase

from sudokulib.backtracking import BacktrackingSolver
from sudokulib.layer import Layer
from sudokulib.preprocessors.line_block import LineBlockPreprocessor

SOLUTION = ' ' * 81


class BacktrackingSolverTestCase(TestCase):
    """Tests for BacktrackingSolver"""

    def test_solver(self):
        solver = BacktrackingSolver()

        data = 'XX4XXX62X76X12X8XXX2XXXX1X74XX9X136223X4X' \
               '65916913524789X3XXX2XX876245913X42XXX7XX'

        layer = Layer(data, SOLUTION)

        self.assertEqual(solver.solve(layer), [
            [8, '9'], [11, '9'], [14, '4'], [17, '5'], [16, '3'], [25, '4'],
            [80, '6'], [62, '4'], [75, '8'], [59, '7'], [57, '6'], [21, '5'],
            [3, '7'], [18, '3'], [20, '8'], [23, '9'], [22, '6'], [38, '7'],
            [29, '5'], [28, '8'], [31, '7'], [40, '8'], [4, '3'], [5, '8'],
            [58, '1'], [55, '5'], [1, '1'], [0, '5'], [61, '8'], [72, '1'],
            [76, '9'], [77, '3'], [79, '5']])


class BacktrackingPreprocessorSolverTestCase(TestCase):
    """Tests for BacktrackingSolver with preprocessors"""

    def test_solver(self):
        solver = BacktrackingSolver([LineBlockPreprocessor])

        data = 'XX4XXX62X76X12X8XXX2XXXX1X74XX9X136223X4X' \
               '65916913524789X3XXX2XX876245913X42XXX7XX'

        layer = Layer(data, SOLUTION)

        self.assertEqual(solver.solve(layer), [
            [4, '3'], [0, '5'], [8, '9'], [11, '9'], [14, '4'], [17, '5'],
            [16, '3'], [18, '3'], [20, '8'], [1, '1'], [23, '9'], [22, '6'],
            [21, '5'], [25, '4'], [38, '7'], [29, '5'], [28, '8'], [31, '7'],
            [40, '8'], [55, '5'], [58, '1'], [61, '8'], [59, '7'], [5, '8'],
            [3, '7'], [57, '6'], [62, '4'], [72, '1'], [75, '8'], [76, '9'],
            [77, '3'], [79, '5'], [80, '6']])
