"""Setup script for bsq"""
import os

from setuptools import setup
from setuptools import find_packages


setup(
    name='sudoku',
    version='0.1',
    zip_safe=False,

    scripts=['./sudokulib/bin/sudoku_solver'],

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
