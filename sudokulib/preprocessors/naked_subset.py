"""Naked Subset Preprocessor for sudokulib"""
from sudokulib.constants import GRID_WIDTH
from sudokulib.constants import REGION_INDEXES
from sudokulib.preprocessors import BasePreprocessor


class NakedSubsetPreprocessor(BasePreprocessor):
    """NakedSubset preprocessor"""
    name = 'Naked Subset'

    def _preprocess(self, layer):
        layer_has_change = False
        for region in ('row', 'col', 'block'):
            for i in range(GRID_WIDTH):
                candidates_indexes = {}
                indexes = REGION_INDEXES[region][i]
                for index in indexes:
                    candidates = layer._candidates[index]
                    candidates = ''.join(sorted(list(candidates)))
                    candidates_indexes.setdefault(candidates, set())
                    candidates_indexes[candidates].add(index)
                for key, item in candidates_indexes.items():
                    key_len = len(key)
                    item_len = len(item)
                    if key_len > 1 and key_len == item_len:
                        key_set = set(key)
                        for index in set(indexes) - item:
                            if key_set & layer._candidates[index]:
                                layer_has_change = True
                                layer._candidates[index] = layer._candidates[
                                    index] - key_set
                if layer_has_change:
                    return layer
