"""Tests for sudokulib.solvers"""
from unittest import TestCase

from sudokulib.layer import Layer
from sudokulib.preprocessors import LineBlockPreprocessor

SOLUTION = ' ' * 81


class LineBlockPreprocessorTestCase(TestCase):
    """Tests for LineBlockPreprocessor"""

    def test_solve(self):
        preprocessor = LineBlockPreprocessor()

        data = '29X7X5X481XX6892738X7X249X5XXX2X1XXXXX24X' \
               '68XXXX98X342X9XX5X2XX44XXXX8X92321947586'

        layer = Layer(data, SOLUTION)
        # TODO write a test
