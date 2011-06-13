"""Preprocessors for sudokulib"""
import logging

logger = logging.getLogger(__name__)


class BasePreprocessor(object):
    """BasePreprocessor class"""
    name = 'base preprocessor'

    def preprocess(self, layer):
        new_layer = self._preprocess(layer)
        if new_layer:
            logger.debug('%s has optimized the layer' % self.name)
            return new_layer
        return None

    def _preprocess(self, layer):
        raise NotImplementedError
