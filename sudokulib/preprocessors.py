"""Preprocessors for sudokulib"""


class BasePreprocessor(object):
    """BasePreprocessor class"""
    name = 'base preprocessor'

    def preprocess(self, layer):
        raise NotImplementedError


class LineBlockPreprocessor(BasePreprocessor):
    """Row/Col Block Interaction preprocessor"""
    name = 'Block Col/Row Interaction'

    def preprocess(self, layer):
        return layer
