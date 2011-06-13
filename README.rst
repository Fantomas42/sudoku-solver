======
SUDOKU
======

Library for solving Sudoku puzzles step by step, in an human manner.

Several scripts are provided to solve directly some grids.

Scripts
=======

sudoku_solver
-------------

Usage: sudoku_indexes [options] source

Script for solving Sudoku puzzles in an human manner, applying
some advanced strategies for solving grids.

If a puzzle cannot be solved with the strategies bundled in the package,
the resolution of the puzzle is done by a backtracking method.

Use the ``--nobacktracking`` option to disable the backtracking method.

Increasing the verbosity level at 3 (``-vvv``) will display step by step
the solving process.


sudoku_backtrack
----------------

Usage: sudoku_backtrack [options] source

Script for solving Sudoku puzzles with the backtracking method only.

Use the ``--nopreprocessing`` option to disable the preprocessing methods
applied to reduces the number of candidates.

This option is useful on small grids where optimisations are not really
needed, but disabling the processings methods on large grid will increase
the resolution time.


sudoku_indexes
--------------

Usage: sudoku_indexes

Display the cells's indexes of a Sudoku puzzle, like they are used in the
package. Very usefull when developing.

Grid files
==========

The files handled by the solvers have to respect some rules to be
processed.

#. The grid file should contains only digits and the *free_char*
   character. By default the **free_char** is represented by a dot *'.'*

#. Everything else will be ignored by default

#. A *0* character is the same as the **free_char**.

#. You can put comments on your grids if a line starts with the *#*
   character.

#. If the grid has a size different than 81, the grid file will not be
   considered as valid.

Example 1
---------

::

  123.56.89578139624496872153952381467641.97835387564291719623548864915372235748916

Example 2
---------

::

  004000620760100800000000107000901300230406091001302000903000000006005013042000700

Example 3
---------

::

  1638.5.7.
  ..8.4..65
  ..5..7..8
  45..82.39
  3.1....4.
  7........
  839.5....
  6.42..59.
  ....93.81


Example 4
---------

::

  3 2 9 | 4 1 . | 7 . .
  . . . | . . . | 4 . .
  . . 5 | . 2 . | . . .
  ---------------------
  5 . . | . . . | 3 . 6
  . 6 . | 7 . 3 | . 9 .
  8 . 7 | . . . | . . 2
  ---------------------
  . . . | . 4 . | 8 . .
  . . 6 | . . . | . . .
  . . 3 | . 7 2 | 9 5 1

Take a look in the ``datas`` folder for more examples.
