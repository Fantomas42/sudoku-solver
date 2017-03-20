"""Setup script for bsq"""
import os

from setuptools import find_packages
from setuptools import setup

import sudokulib


setup(
    name='sudoku-solver',
    version=sudokulib.__version__,
    zip_safe=False,

    test_suite='sudokulib.tests.test_suite',
    scripts=['./sudokulib/scripts/sudoku_solver',
             './sudokulib/scripts/sudoku_backtrack',
             './sudokulib/scripts/sudoku_solver_benchmark',
             './sudokulib/scripts/sudoku_indexes'],

    packages=find_packages(exclude=['tests']),
    include_package_data=True,

    author=sudokulib.__author__,
    author_email=sudokulib.__email__,
    url=sudokulib.__url__,

    license=sudokulib.__license__,
    platforms='any',
    description='Library and scripts for solving Sudoku puzzles.',
    long_description=open(os.path.join('README.rst')).read(),
    keywords='sudoku, solver',
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    )
