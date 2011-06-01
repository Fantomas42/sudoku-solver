"""Disjoint Chain Preprocessor for sudokulib"""
from sudokulib.preprocessors import BasePreprocessor


class DisjointChainPreprocessor(BasePreprocessor):
    """DisjointChain preprocessor"""
    name = 'Disjoint Chain'

    def preprocess(self, layer):
        return None
