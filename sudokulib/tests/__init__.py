"""Tests for sudokulib"""
import unittest

from sudokulib.tests.layer import LayerTestCase
from sudokulib.tests.layer import AdvancedLayerTestCase
from sudokulib.tests.solvers import SingletonSolverTestCase
from sudokulib.tests.solvers import NakedSingletonSolverTestCase
from sudokulib.tests.solvers import HiddenSingletonSolverTestCase
from sudokulib.tests.preprocessors import LineBlockPreprocessorTestCase

loader = unittest.TestLoader()

test_suite = unittest.TestSuite([
    loader.loadTestsFromTestCase(LayerTestCase),
    loader.loadTestsFromTestCase(AdvancedLayerTestCase),
    loader.loadTestsFromTestCase(SingletonSolverTestCase),
    loader.loadTestsFromTestCase(NakedSingletonSolverTestCase),
    loader.loadTestsFromTestCase(HiddenSingletonSolverTestCase),
    loader.loadTestsFromTestCase(LineBlockPreprocessorTestCase),
    ])
