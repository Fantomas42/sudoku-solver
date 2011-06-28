"""Tests for sudokulib"""
import unittest

from sudokulib.tests.grid import BaseGridTestCase
from sudokulib.tests.grid import StringGridTestCase
from sudokulib.tests.grid import FileSystemGridTestCase
from sudokulib.tests.layer import LayerTestCase
from sudokulib.tests.layer import AdvancedLayerTestCase
from sudokulib.tests.solver import SudokuSolverTestCase
from sudokulib.tests.solvers import BaseSolverTestCase
from sudokulib.tests.solvers import SingletonSolverTestCase
from sudokulib.tests.solvers import NakedSingletonSolverTestCase
from sudokulib.tests.solvers import HiddenSingletonSolverTestCase
from sudokulib.tests.backtracking import BacktrackingSolverTestCase
from sudokulib.tests.backtracking import BacktrackingPreprocessorSolverTestCase
from sudokulib.tests.preprocessors import BasePreprocessorTestCase
from sudokulib.tests.preprocessors import LineBlockPreprocessorTestCase
from sudokulib.tests.preprocessors import BlockBlockPreprocessorTestCase
from sudokulib.tests.preprocessors import NakedSubsetPreprocessorTestCase
from sudokulib.tests.preprocessors import DisjointChainPreprocessorTestCase

loader = unittest.TestLoader()

test_suite = unittest.TestSuite([
    loader.loadTestsFromTestCase(BaseGridTestCase),
    loader.loadTestsFromTestCase(StringGridTestCase),
    loader.loadTestsFromTestCase(FileSystemGridTestCase),
    loader.loadTestsFromTestCase(LayerTestCase),
    loader.loadTestsFromTestCase(AdvancedLayerTestCase),
    loader.loadTestsFromTestCase(BaseSolverTestCase),
    loader.loadTestsFromTestCase(SingletonSolverTestCase),
    loader.loadTestsFromTestCase(NakedSingletonSolverTestCase),
    loader.loadTestsFromTestCase(HiddenSingletonSolverTestCase),
    loader.loadTestsFromTestCase(BacktrackingSolverTestCase),
    loader.loadTestsFromTestCase(BacktrackingPreprocessorSolverTestCase),
    loader.loadTestsFromTestCase(BasePreprocessorTestCase),
    loader.loadTestsFromTestCase(LineBlockPreprocessorTestCase),
    loader.loadTestsFromTestCase(BlockBlockPreprocessorTestCase),
    loader.loadTestsFromTestCase(NakedSubsetPreprocessorTestCase),
    loader.loadTestsFromTestCase(DisjointChainPreprocessorTestCase),
    loader.loadTestsFromTestCase(SudokuSolverTestCase),
    ])
