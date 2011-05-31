"""Setup script for bsq"""
import os

from setuptools import setup
from setuptools import find_packages


setup(
    name='sudoku',
    version='0.1',
    zip_safe=False,

    test_suite='sudokulib.tests.test_suite',
    scripts=['./sudokulib/scripts/sudoku_solver',
             './sudokulib/scripts/sudoku_backtrack',
             './sudokulib/scripts/sudoku_indexes'],

    packages=find_packages(exclude=['tests']),
    include_package_data=True,

    author='Fantomas42',
    author_email='fantomas42@gmail.com',
    url='http://fantomas.willbreak.it/',

    license='GPL',
    platforms='any',
    description='Sudoku solver.',
    long_description=open(os.path.join('README.rst')).read(),
    keywords='sudoku, solver',
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    )
