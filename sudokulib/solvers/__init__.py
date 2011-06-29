"""Solvers for sudokulib"""
import logging

logger = logging.getLogger(__name__)


class BaseSolver(object):
    """BaseSolver class"""
    name = 'base solver'

    def solve(self, layer, index):
        """If a solution has been found, log it
        and return it"""
        solution = self._solve(layer, index)
        if solution:
            logger.debug("%s has found solution '%s' at index %s" % (
                self.name, solution, index))
            return solution

    def _solve(self, layer, index):
        raise NotImplementedError
