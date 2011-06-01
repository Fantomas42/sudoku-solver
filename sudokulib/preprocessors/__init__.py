"""Preprocessors for sudokulib"""


class BasePreprocessor(object):
    """BasePreprocessor class"""
    name = 'base preprocessor'

    def preprocess(self, layer):
        raise NotImplementedError
