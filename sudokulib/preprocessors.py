"""Preprocessors for sudokulib"""
from sudokulib.constants import GRID_WIDTH
from sudokulib.constants import BLOCK_WIDTH
from sudokulib.constants import INDEX_REGIONS
from sudokulib.constants import REGION_INDEXES


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
            # Start implement rows check
            offset = 0
            for j in range(BLOCK_WIDTH):
                index_1 = (i * GRID_WIDTH) + offset
                index_2 = index_1 + 1
                index_3 = index_2 + 1
                index_1_candidates = layer._candidates[index_1]
                index_2_candidates = layer._candidates[index_2]
                index_3_candidates = layer._candidates[index_3]

                twins = False
                if index_1_candidates & index_2_candidates:
                    twins = (index_1, index_2)
                    twins_candidates = index_1_candidates & index_2_candidates
                elif index_2_candidates & index_3_candidates:
                    twins = (index_2, index_3)
                    twins_candidates = index_2_candidates & index_3_candidates
                elif index_1_candidates & index_3_candidates:
                    twins = (index_1, index_3)
                    twins_candidates = index_1_candidates & index_3_candidates

                offset += BLOCK_WIDTH

                if not twins:
                    continue

                block_index = INDEX_REGIONS[index_1]['block']
                block_other_indexes = set(REGION_INDEXES['block'][block_index]) - \
                                      set([index_1, index_2, index_3])
                all_candidates = set()
                for index in block_other_indexes:
                    all_candidates |= layer._candidates[index]

                twin_candidates_valids = []
                for twin_candidate in twins_candidates:
                    if not twin_candidate in all_candidates:
                        twin_candidates_valids.append(twin_candidate)

                if not twin_candidates_valids:
                    continue

                line_other_indexes = INDEX_REGIONS[index_1]['row']
                line_other_indexes = set(REGION_INDEXES['row'][i]) - \
                                     set([index_1, index_2, index_3])
                layer_has_changed = False
                for index in line_other_indexes:
                    for candidate_to_remove in twin_candidates_valids:
                        if candidate_to_remove in layer._candidates[index]:
                            layer_has_changed = True
                            layer._candidates[index] = layer._candidates[index] - \
                                                       set([candidate_to_remove])

                if layer_has_changed:
                    return layer

        # Cols check =========================================

        for i in range(GRID_WIDTH):
            offset = 0
            for j in range(BLOCK_WIDTH):
                index_1 = i + offset
                index_2 = index_1 + GRID_WIDTH
                index_3 = index_2 + GRID_WIDTH
                index_1_candidates = layer._candidates[index_1]
                index_2_candidates = layer._candidates[index_2]
                index_3_candidates = layer._candidates[index_3]

                twins = False
                if index_1_candidates & index_2_candidates:
                    twins = (index_1, index_2)
                    twins_candidates = index_1_candidates & index_2_candidates
                elif index_2_candidates & index_3_candidates:
                    twins = (index_2, index_3)
                    twins_candidates = index_2_candidates & index_3_candidates
                elif index_1_candidates & index_3_candidates:
                    twins = (index_1, index_3)
                    twins_candidates = index_1_candidates & index_3_candidates

                offset += BLOCK_WIDTH * GRID_WIDTH

                if not twins:
                    continue

                block_index = INDEX_REGIONS[index_1]['block']
                block_other_indexes = set(REGION_INDEXES['block'][block_index]) - \
                                      set([index_1, index_2, index_3])
                all_candidates = set()
                for index in block_other_indexes:
                    all_candidates |= layer._candidates[index]

                twin_candidates_valids = []
                for twin_candidate in twins_candidates:
                    if not twin_candidate in all_candidates:
                        twin_candidates_valids.append(twin_candidate)

                if not twin_candidates_valids:
                    continue

                line_other_indexes = INDEX_REGIONS[index_1]['col']
                line_other_indexes = set(REGION_INDEXES['col'][i]) - \
                                     set([index_1, index_2, index_3])
                layer_has_changed = False
                for index in line_other_indexes:
                    for candidate_to_remove in twin_candidates_valids:
                        if candidate_to_remove in layer._candidates[index]:
                            layer_has_changed = True
                            layer._candidates[index] = layer._candidates[index] - \
                                                       set([candidate_to_remove])

                if layer_has_changed:
                    return layer

        return None
