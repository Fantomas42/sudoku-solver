"""Tests for Layer"""
from unittest import TestCase

from sudokulib.layer import Layer

DATA_SET = '1234567X9234567891345678912456789X2356789' \
           '1234678912345789123456891234567912345678'
SOLUTION = '       8                         1       ' \
           '                                        '

#  Visualization :
#
#  123 | 456 | 789
#  234 | 567 | 891
#  345 | 678 | 912
#  ---------------
#  456 | 789 | 123
#  567 | 891 | 234
#  678 | 912 | 345
#  ---------------
#  789 | 123 | 456
#  891 | 234 | 567
#  912 | 345 | 678
#
#  Note this is not a valid puzzle


class LayerTestCase(TestCase):

    def setUp(self):
        self.layer = Layer(DATA_SET, SOLUTION)

    def test_str(self):
        self.assertEquals(self.layer.str,
                          '12345678923456789134567891245678912356789' \
                          '1234678912345789123456891234567912345678')

    def test_row_table(self):
        self.assertEquals(self.layer.row_table[0], ['1', '2', '3',
                                                    '4', '5', '6',
                                                    '7', '8', '9'])
        self.assertEquals(self.layer.row_table[1], ['2', '3', '4',
                                                    '5', '6', '7',
                                                    '8', '9', '1'])
        self.assertEquals(self.layer.row_table[8], ['9', '1', '2',
                                                    '3', '4', '5',
                                                    '6', '7', '8'])

    def test_col_table(self):
        self.assertEquals(self.layer.col_table[0], ['1', '2', '3',
                                                    '4', '5', '6',
                                                    '7', '8', '9'])
        self.assertEquals(self.layer.col_table[1], ['2', '3', '4',
                                                    '5', '6', '7',
                                                    '8', '9', '1'])
        self.assertEquals(self.layer.row_table[8], ['9', '1', '2',
                                                    '3', '4', '5',
                                                    '6', '7', '8'])

    def test_block_table(self):
        self.assertEquals(self.layer.block_table[0], ['1', '2', '3',
                                                      '2', '3', '4',
                                                      '3', '4', '5'])
        self.assertEquals(self.layer.block_table[4], ['7', '8', '9',
                                                      '8', '9', '1',
                                                      '9', '1', '2'])
        self.assertEquals(self.layer.block_table[8], ['4', '5', '6',
                                                      '5', '6', '7',
                                                      '6', '7', '8'])
