"""Preprocessors for sudokulib"""
from sudokulib.constants import GRID_WIDTH
from sudokulib.constants import BLOCK_WIDTH


class BasePreprocessor(object):
    """BasePreprocessor class"""
    name = 'base preprocessor'

    def preprocess(self, layer):
        raise NotImplementedError


class LineBlockPreprocessor(BasePreprocessor):
    """Row/Col Block Interaction preprocessor"""
    name = 'Block Col/Row Interaction'

    def preprocess(self, layer):
        # Detecter un jumeau ou triple dans les regions
        #   => Un jumeau est 2 candidats qui se suivent sur une ligne
        #      ou une colonne nul par ailleurs dans une region
        # Si jumeau ou triple :
        #   Supprimer les candidats de la ligne/colonne hors de la region


        for i in range(GRID_WIDTH):
            pass


        return None
