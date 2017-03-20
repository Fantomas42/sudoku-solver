"""Tests for Grid"""
import os
import tempfile
from unittest import TestCase

from sudokulib.grid import BaseGrid
from sudokulib.grid import FileSystemGrid
from sudokulib.grid import InvalidGrid
from sudokulib.grid import StringGrid
from sudokulib.layer import Layer


class BaseGridTestCase(TestCase):

    def test_load_source(self):
        self.assertRaises(NotImplementedError, BaseGrid, 'filename')


class StringGridTestCase(TestCase):
    grid_str = '1638.5.7...8.4..65..5..7..845..82.393.1..' \
               '..4.7........839.5....6.42..59.....93.81'

    def test_load_source(self):
        grid = StringGrid(self.grid_str, '.')
        self.assertEqual(grid.data,
                         '1638X5X7XXX8X4XX65XX5XX7XX845XX82X393X1XX'
                         'XX4X7XXXXXXXX839X5XXXX6X42XX59XXXXX93X81')
        grid = StringGrid(self.grid_str, '@')
        self.assertEqual(grid.data,
                         '1638.5.7...8.4..65..5..7..845..82.393.1..'
                         '..4.7........839.5....6.42..59.....93.81')
        grid = StringGrid(self.grid_str, '.', '@')
        self.assertEqual(grid.data,
                         '1638@5@7@@@8@4@@65@@5@@7@@845@@82@393@1@@'
                         '@@4@7@@@@@@@@839@5@@@@6@42@@59@@@@@93@81')

    def test_validate(self):
        grid = StringGrid(self.grid_str)
        self.assertEqual(grid.validate(), True)
        grid = StringGrid(self.grid_str[:-1])
        self.assertRaises(InvalidGrid, grid.validate)
        grid = StringGrid('0' * 81)
        self.assertRaises(InvalidGrid, grid.validate)
        grid = StringGrid('12333000000000000000000000000000000000000'
                          '0000000237777777777777777777900000000000')
        self.assertRaises(InvalidGrid, grid.validate)

    def test_missing(self):
        grid = StringGrid(self.grid_str)
        self.assertEqual(grid.missing, 45)

    def test_completed(self):
        grid = StringGrid(self.grid_str)
        self.assertEqual(grid.completed, False)
        grid.data_solution = '1' * 81
        self.assertEqual(grid.completed, True)

    def test_layer(self):
        grid = StringGrid(self.grid_str)
        self.assertEqual(type(grid.layer), Layer)

    def test_apply_solutions(self):
        grid = StringGrid(self.grid_str)
        self.assertEqual(grid.data_solution,
                         '    X X XXX X XX  XX XX XX   XX  X   X XX'
                         'XX X XXXXXXXX   X XXXX X  XX  XXXXX  X  ')
        grid.apply_solutions([(4, 1), (6, '8')])
        self.assertEqual(grid.data_solution,
                         '    1 8 XXX X XX  XX XX XX   XX  X   X XX'
                         'XX X XXXXXXXX   X XXXX X  XX  XXXXX  X  ')

    def test__len__(self):
        grid = StringGrid(self.grid_str)
        self.assertEqual(len(grid), 81)


class FileSystemGridTestCase(TestCase):

    grid_str = """
# This is a grid
...|...|...
.9.|.3.|.4.
..2|6.1|5..
-----------
..4|...|2..
.3.|.5.|.1.
..6|...|7..
-----------
..5|8.2|6..
.7.|.4.|.9.
...|...|...
"""

    def test_load_source(self):
        grid_file_fd_no, grid_file_path = tempfile.mkstemp()

        grid_file = os.fdopen(grid_file_fd_no, 'w')
        grid_file.write(self.grid_str)
        grid_file.close()

        grid = FileSystemGrid(grid_file_path)

        try:
            self.assertEqual(grid.data,
                             'XXXXXXXXXX9XX3XX4XXX26X15XXXX4XXX2XXX3XX5'
                             'XX1XXX6XXX7XXXX58X26XXX7XX4XX9XXXXXXXXXX')
        finally:
            os.remove(grid_file_path)
