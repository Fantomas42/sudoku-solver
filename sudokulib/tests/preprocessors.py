"""Tests for sudokulib.solvers"""
from unittest import TestCase

from sudokulib.layer import Layer
from sudokulib.preprocessors import BasePreprocessor
from sudokulib.preprocessors.block_block import BlockBlockPreprocessor
from sudokulib.preprocessors.disjoint_chain import DisjointChainPreprocessor
from sudokulib.preprocessors.line_block import LineBlockPreprocessor
from sudokulib.preprocessors.naked_subset import NakedSubsetPreprocessor

SOLUTION = ' ' * 81


class BasePreprocessorTestCase(TestCase):
    """Tests for BasePreprocessor"""

    def test_preprocess(self):
        preprocessor = BasePreprocessor()

        layer = Layer(SOLUTION, SOLUTION)
        self.assertRaises(NotImplementedError, preprocessor.preprocess, layer)


class LineBlockPreprocessorTestCase(TestCase):
    """Tests for LineBlockPreprocessor"""

    def test_preprocess_horizontal(self):
        preprocessor = LineBlockPreprocessor()

        data = '29X7X5X481XX6892738X7X249X5XXX2X1XXXXX24X' \
               '68XXXX98X342X9XX5X2XX44XXXX8X92321947586'

        layer = Layer(data, SOLUTION)
        self.assertEqual(layer._candidates[27], set(['5', '6', '7']))
        self.assertEqual(layer._candidates[28], set(['3', '4', '5',
                                                     '6', '7', '8']))
        self.assertEqual(layer._candidates[29], set(['3', '4', '5',
                                                     '6', '8']))
        self.assertEqual(layer._candidates[33], set(['3', '6', '7']))
        self.assertEqual(layer._candidates[34], set(['3', '5', '6']))
        self.assertEqual(layer._candidates[35], set(['7', '9']))

        layer = preprocessor.preprocess(layer)
        self.assertEqual(layer._candidates[27], set(['5', '7']))
        self.assertEqual(layer._candidates[28], set(['3', '4', '5',
                                                     '7', '8']))
        self.assertEqual(layer._candidates[29], set(['3', '4', '5', '8']))
        self.assertEqual(layer._candidates[33], set(['3', '6', '7']))
        self.assertEqual(layer._candidates[34], set(['3', '5', '6']))
        self.assertEqual(layer._candidates[35], set(['7', '9']))

    def test_preprocess_vertical(self):
        preprocessor = LineBlockPreprocessor()

        data = '29X7X5X481XX6892738X7X249X5XXX2X1XXXXX24X' \
               '68XX6X98X342X9XX5X2XX44XXXX8X92321947586'

        layer = Layer(data, SOLUTION)
        self.assertEqual(layer._candidates[28], set(['3', '4', '5',
                                                     '7', '8']))
        self.assertEqual(layer._candidates[37], set(['1', '3', '5', '7']))
        self.assertEqual(layer._candidates[46], set(['1', '5', '7']))
        self.assertEqual(layer._candidates[55], set(['6', '7', '8']))
        self.assertEqual(layer._candidates[64], set(['5', '6', '7']))

        layer = preprocessor.preprocess(layer)
        self.assertEqual(layer._candidates[28], set(['3', '4', '5', '8']))
        self.assertEqual(layer._candidates[37], set(['1', '3', '5']))
        self.assertEqual(layer._candidates[46], set(['1', '5']))
        self.assertEqual(layer._candidates[55], set(['6', '7', '8']))
        self.assertEqual(layer._candidates[64], set(['5', '6', '7']))

    def test_preprocess_failing(self):
        preprocessor = LineBlockPreprocessor()

        data = '3XXX3X81XX28X1X7X41X78XX2XX2X917X3XXX56XX' \
               'X1X7731X8X4X2XXXX4192XX1X96X5XXXXXX5X6X1'

        layer = Layer(data, SOLUTION)
        self.assertEqual(layer._candidates[16], set(['3', '5', '6', '9']))
        self.assertEqual(layer._candidates[25], set(['3', '5', '6', '9']))
        self.assertEqual(layer._candidates[34], set(['5', '6', '8']))
        self.assertEqual(layer._candidates[43], set(['8', '9']))
        self.assertEqual(layer._candidates[52], set(['5', '6', '9']))
        self.assertEqual(layer._candidates[70], set(['3', '4', '7', '8']))
        self.assertEqual(layer._candidates[79], set(['3', '4', '7', '8']))

        layer = preprocessor.preprocess(layer)
        self.assertEqual(layer._candidates[16], set(['3', '5', '6']))
        self.assertEqual(layer._candidates[25], set(['3', '5', '6']))
        self.assertEqual(layer._candidates[34], set(['5', '6', '8']))
        self.assertEqual(layer._candidates[43], set(['8', '9']))
        self.assertEqual(layer._candidates[52], set(['5', '6', '9']))
        self.assertEqual(layer._candidates[70], set(['3', '4', '7', '8']))
        self.assertEqual(layer._candidates[79], set(['3', '4', '7', '8']))


class BlockBlockPreprocessorTestCase(TestCase):
    """Tests for BlockBlockPreprocessor"""

    def test_preprocess_horizontal(self):
        preprocessor = BlockBlockPreprocessor()

        data = 'XX5X7X89XX198X2XX5487XXXXX2XX3XXX5X8954X8' \
               'XX26XX8XXX9XX541798263732465189896X2X457'

        layer = Layer(data, SOLUTION)
        self.assertEqual(layer._candidates[30], set(['1', '2', '6', '9']))
        self.assertEqual(layer._candidates[31], set(['1', '4']))
        self.assertEqual(layer._candidates[32], set(['1', '4', '6',
                                                     '7', '9']))
        self.assertEqual(layer._candidates[48], set(['1', '2', '3',
                                                     '5', '6']))
        self.assertEqual(layer._candidates[49], set(['1', '3', '4', '5']))
        self.assertEqual(layer._candidates[50], set(['1', '3', '4',
                                                     '6', '7']))

        layer = preprocessor.preprocess(layer)
        self.assertEqual(layer._candidates[30], set(['2', '6', '9']))
        self.assertEqual(layer._candidates[31], set(['4']))
        self.assertEqual(layer._candidates[32], set(['4', '6', '7', '9']))
        self.assertEqual(layer._candidates[48], set(['2', '3', '5', '6']))
        self.assertEqual(layer._candidates[49], set(['3', '4', '5']))
        self.assertEqual(layer._candidates[50], set(['3', '4', '6', '7']))

    def test_preprocess_horizontal_for_coverage(self):
        preprocessor = BlockBlockPreprocessor()

        data = '7X94X85X64XXXX69X7X6X79X4839X46XX87587XX4' \
               'X692625987341396871254XXX264739247359168'

        layer = Layer(data, SOLUTION)
        layer = LineBlockPreprocessor().preprocess(layer)
        self.assertEqual(layer._candidates[1], set(['1', '3']))
        self.assertEqual(layer._candidates[10], set(['1', '3', '5', '8']))
        self.assertEqual(layer._candidates[11], set(['1', '2', '3', '8']))

        layer = preprocessor.preprocess(layer)
        self.assertEqual(layer._candidates[1], set(['3']))
        self.assertEqual(layer._candidates[10], set(['3', '5', '8']))
        self.assertEqual(layer._candidates[11], set(['2', '3', '8']))

        data = data[::-1]

        layer = Layer(data, SOLUTION)
        layer = LineBlockPreprocessor().preprocess(layer)
        self.assertEqual(layer._candidates[79], set(['1', '3']))
        self.assertEqual(layer._candidates[70], set(['1', '3', '5', '8']))
        self.assertEqual(layer._candidates[69], set(['1', '2', '3', '8']))

        layer = preprocessor.preprocess(layer)
        self.assertEqual(layer._candidates[79], set(['3']))
        self.assertEqual(layer._candidates[70], set(['3', '5', '8']))
        self.assertEqual(layer._candidates[69], set(['2', '3', '8']))

    def test_preprocess_vertical(self):
        preprocessor = BlockBlockPreprocessor()

        data = '29X7X5X481XX6892738X7X249X5XXX2X1XXXXX24X' \
               '68XX6X98X342X9XX5X2XX44XXXX8X92321947586'

        layer = Layer(data, SOLUTION)
        layer = LineBlockPreprocessor().preprocess(layer)
        layer = LineBlockPreprocessor().preprocess(layer)
        self.assertEqual(layer._candidates[28], set(['3', '4', '5', '8']))
        self.assertEqual(layer._candidates[29], set(['3', '4', '5', '8']))
        self.assertEqual(layer._candidates[37], set(['1', '3', '5']))
        self.assertEqual(layer._candidates[46], set(['1', '5']))

        layer = preprocessor.preprocess(layer)
        self.assertEqual(layer._candidates[28], set(['3', '4', '8']))
        self.assertEqual(layer._candidates[29], set(['3', '4', '8']))
        self.assertEqual(layer._candidates[37], set(['1', '3']))
        self.assertEqual(layer._candidates[46], set(['1']))


class NakedSubsetPreprocessorTestCase(TestCase):
    """Tests for NakedSubsetPreprocessor"""

    def test_preprocess(self):
        preprocessor = NakedSubsetPreprocessor()

        data = '3XXX2X81XX28X1X7X41X78XX2XX2X917X3XXX56XX' \
               'X1X7731X8X4X2XXXX4192XX1X96X5XXXXXX5X6X1'

        layer = Layer(data, SOLUTION)
        self.assertEqual(layer._candidates[9], set(['5', '6', '9']))
        self.assertEqual(layer._candidates[36], set(['4', '8']))
        self.assertEqual(layer._candidates[54], set(['5', '6', '8']))
        self.assertEqual(layer._candidates[63], set(['4', '8']))
        self.assertEqual(layer._candidates[72], set(['4', '8', '9']))

        layer = preprocessor.preprocess(layer)
        self.assertEqual(layer._candidates[9], set(['5', '6', '9']))
        self.assertEqual(layer._candidates[36], set(['4', '8']))
        self.assertEqual(layer._candidates[54], set(['5', '6']))
        self.assertEqual(layer._candidates[63], set(['4', '8']))
        self.assertEqual(layer._candidates[72], set(['9']))


class DisjointChainPreprocessorTestCase(TestCase):
    """Tests for DisjointChainPreprocessor"""

    def test_preprocess(self):
        preprocessor = DisjointChainPreprocessor()

        data = 'XX4XXX62X76X12X8XXX2XXXX1X74XX9X136223X4X' \
               '65916913524789X3XXX2XX876245913X42XXX7XX'

        layer = Layer(data, SOLUTION)
        layer = LineBlockPreprocessor().preprocess(layer)
        self.assertEqual(layer._candidates[72], set(['1', '5']))
        self.assertEqual(layer._candidates[75], set(['6', '8']))
        self.assertEqual(layer._candidates[76], set(['1', '3', '6', '9']))
        self.assertEqual(layer._candidates[77], set(['3', '8', '9']))
        self.assertEqual(layer._candidates[79], set(['5', '8']))
        self.assertEqual(layer._candidates[80], set(['5', '6']))

        layer = preprocessor.preprocess(layer)
#         self.assertEqual(layer._candidates[72], set(['1']))
#         self.assertEqual(layer._candidates[75], set(['6', '8']))
#         self.assertEqual(layer._candidates[76], set(['1', '3', '9']))
#         self.assertEqual(layer._candidates[77], set(['3', '9']))
#         self.assertEqual(layer._candidates[79], set(['5', '8']))
#         self.assertEqual(layer._candidates[80], set(['5', '6']))
