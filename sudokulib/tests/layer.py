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
        self.assertEqual(str(self.layer),
                         '12345678923456789134567891245678912356789'
                         '1234678912345789123456891234567912345678')

    def test_get_region_row(self):
        self.assertEqual(self.layer.get_region('row', 1),
                         ['1', '2', '3',
                          '4', '5', '6',
                          '7', '8', '9'])
        self.assertEqual(self.layer.get_region('row', 7),
                         ['1', '2', '3',
                          '4', '5', '6',
                          '7', '8', '9'])
        self.assertEqual(self.layer.get_region('row', 37),
                         ['5', '6', '7',
                          '8', '9', '1',
                          '2', '3', '4'])
        self.assertEqual(self.layer.get_region('row', 78),
                         ['9', '1', '2',
                          '3', '4', '5',
                          '6', '7', '8'])

    def test_get_region_col(self):
        self.assertEqual(self.layer.get_region('col', 0),
                         ['1', '2', '3',
                          '4', '5', '6',
                          '7', '8', '9'])
        self.assertEqual(self.layer.get_region('col', 7),
                         ['8', '9', '1',
                          '2', '3', '4',
                          '5', '6', '7'])
        self.assertEqual(self.layer.get_region('col', 37),
                         ['2', '3', '4',
                          '5', '6', '7',
                          '8', '9', '1'])
        self.assertEqual(self.layer.get_region('col', 78),
                         ['7', '8', '9',
                          '1', '2', '3',
                          '4', '5', '6'])

    def test_get_region_block(self):
        self.assertEqual(self.layer.get_region('block', 1),
                         ['1', '2', '3',
                          '2', '3', '4',
                          '3', '4', '5'])
        self.assertEqual(self.layer.get_region('block', 7),
                         ['7', '8', '9',
                          '8', '9', '1',
                          '9', '1', '2'])
        self.assertEqual(self.layer.get_region('block', 37),
                         ['4', '5', '6',
                          '5', '6', '7',
                          '6', '7', '8'])
        self.assertEqual(self.layer.get_region('block', 48),
                         ['7', '8', '9',
                          '8', '9', '1',
                          '9', '1', '2'])
        self.assertEqual(self.layer.get_region('block', 73),
                         ['7', '8', '9',
                          '8', '9', '1',
                          '9', '1', '2'])
        self.assertEqual(self.layer.get_region('block', 78),
                         ['4', '5', '6',
                          '5', '6', '7',
                          '6', '7', '8'])

    def test_get_region_index(self):
        self.assertRaises(KeyError, self.layer.get_region_index,
                          'toto', 12)
        self.assertEqual(self.layer.get_region_index('row', 0), 0)
        self.assertEqual(self.layer.get_region_index('col', 0), 0)
        self.assertEqual(self.layer.get_region_index('block', 0), 0)

        self.assertEqual(self.layer.get_region_index('row', 1), 0)
        self.assertEqual(self.layer.get_region_index('col', 1), 1)
        self.assertEqual(self.layer.get_region_index('block', 1), 0)

        self.assertEqual(self.layer.get_region_index('row', 17), 1)
        self.assertEqual(self.layer.get_region_index('col', 17), 8)
        self.assertEqual(self.layer.get_region_index('block', 17), 2)

        self.assertEqual(self.layer.get_region_index('row', 42), 4)
        self.assertEqual(self.layer.get_region_index('col', 42), 6)
        self.assertEqual(self.layer.get_region_index('block', 42), 5)

        self.assertEqual(self.layer.get_region_index('row', 78), 8)
        self.assertEqual(self.layer.get_region_index('col', 78), 6)
        self.assertEqual(self.layer.get_region_index('block', 78), 8)


class AdvancedLayerTestCase(TestCase):

    def test_get_region_missing_indexes(self):
        layer = Layer(DATA_SET, ' ' * 81)
        self.assertEqual(layer.get_region_missing_indexes('row', 1), [7])
        self.assertEqual(layer.get_region_missing_indexes('col', 79), [7])
        self.assertEqual(layer.get_region_missing_indexes('block', 16), [7])

        self.assertEqual(layer.get_region_missing_indexes('row', 30), [33])
        self.assertEqual(layer.get_region_missing_indexes('col', 15), [33])
        self.assertEqual(layer.get_region_missing_indexes('block', 35), [33])

        self.assertEqual(layer.get_region_missing_indexes('row', 7), [])
        self.assertEqual(layer.get_region_missing_indexes('col', 7), [])
        self.assertEqual(layer.get_region_missing_indexes('block', 1), [])

    def test_get_excluded(self):
        layer = Layer(DATA_SET, ' ' * 81)
        self.assertEqual(layer.get_excluded(7),
                         set(['1', '2', '3', '4', '5',
                              '6', '7', '8', '9', 'X']))

    def test_get_candidates(self):
        layer = Layer(DATA_SET, ' ' * 81)
        self.assertEqual(layer.get_candidates(7),
                         set())
        self.assertEqual(layer.get_candidates(8),
                         set())
