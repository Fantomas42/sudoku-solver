"""Tests for sudokulib"""
import unittest

from sudokulib.tests.layer import LayerTestCase
from sudokulib.tests.layer import AdvancedLayerTestCase
from sudokulib.tests.solvers import BaseSolverTestCase
from sudokulib.tests.solvers import SingletonSolverTestCase
from sudokulib.tests.solvers import NakedSingletonSolverTestCase
from sudokulib.tests.solvers import HiddenSingletonSolverTestCase
from sudokulib.tests.preprocessors import BasePreprocessorTestCase
from sudokulib.tests.preprocessors import LineBlockPreprocessorTestCase
from sudokulib.tests.preprocessors import BlockBlockPreprocessorTestCase
from sudokulib.tests.preprocessors import NakedSubsetPreprocessorTestCase
#from sudokulib.tests.preprocessors import DisjointChainPreprocessorTestCase

loader = unittest.TestLoader()

test_suite = unittest.TestSuite([
    loader.loadTestsFromTestCase(LayerTestCase),
    loader.loadTestsFromTestCase(AdvancedLayerTestCase),
    loader.loadTestsFromTestCase(BaseSolverTestCase),
    loader.loadTestsFromTestCase(SingletonSolverTestCase),
    loader.loadTestsFromTestCase(NakedSingletonSolverTestCase),
    loader.loadTestsFromTestCase(HiddenSingletonSolverTestCase),
    loader.loadTestsFromTestCase(BasePreprocessorTestCase),
    loader.loadTestsFromTestCase(LineBlockPreprocessorTestCase),
    loader.loadTestsFromTestCase(BlockBlockPreprocessorTestCase),
    loader.loadTestsFromTestCase(NakedSubsetPreprocessorTestCase),
    #loader.loadTestsFromTestCase(DisjointChainPreprocessorTestCase),
    ])
