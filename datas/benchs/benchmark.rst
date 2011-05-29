Test solver datas/medium/03.grid
================================

Temps initial : 0.49
Graph 	      : 8.57


1er optim :
-----------

1 Seul Layer par tour à la place 1 layer par instanciation
de solver

Temps initial : 0.18
Graph 	      : 6.45


2eme optim :
------------

Simplification instanciation Solvers.

Temps initial : 0.17
Graph	      : 6.30


3eme optim :
------------

Hard linking INDEX_REGION

Temps initial : 0.15
Graph 	      : 6.12


4eme optim :
------------

All is hardlinked.

Temps initial : 0.18
Graph 	      : 6.13

ERF

5eme optim :
------------

Not using get_region_index

Temps initial : 0.17
Graph 	      : 4.17

6eme optim :
------------

Precalculing all datas

Temps initial : 0.049
Graph 	      : 1.25

7eme optim :
------------

Hard linking solvers

Temps initial : 0.045
Graph 	      : 0.67

8eme optim :
------------

Disable SingletonSolver

Temps initial : 0.039
Graph 	      : 0.67

9eme optim :
------------

Rewrite solvers with hard linking

Temps initial : 0.032
Graph 	      ; 0.037

Add Feature :
-------------

Col/Row Preprocessor

Temps initial : 0.060
Graph 	      : 0.76


Add Feature :
-------------

Block/Block Preprocessor

Temps initial : 0.070
Graph 	      : 1.07
