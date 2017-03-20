"""LineBlock Preprocessor for sudokulib"""
from sudokulib.constants import BLOCK_WIDTH
from sudokulib.constants import GRID_WIDTH
from sudokulib.constants import INDEX_REGIONS
from sudokulib.constants import REGION_INDEXES
from sudokulib.preprocessors import BasePreprocessor


class LineBlockPreprocessor(BasePreprocessor):
    """Row/Col Block Interaction preprocessor"""
    name = 'Block Col/Row Interaction'

    def _preprocess(self, layer):
        """
        Detect a Twin in the regions vertically and horizontally:
          => A Twin represent 2 candidates in a region and
             in a col or a row, and nowhere else in the region.
          If some Twins are detected:
            Remove the Twins in the candidates of the col or row
            outside the region.
        """

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

                twins_candidates = set()
                if index_1_candidates & index_2_candidates:
                    twins_candidates |= index_1_candidates & index_2_candidates
                if index_2_candidates & index_3_candidates:
                    twins_candidates |= index_2_candidates & index_3_candidates
                if index_1_candidates & index_3_candidates:
                    twins_candidates |= index_1_candidates & index_3_candidates

                offset += BLOCK_WIDTH

                if not twins_candidates:
                    continue

                all_candidates = set()
                block_index = INDEX_REGIONS[index_1]['block']
                for index in set(REGION_INDEXES['block'][block_index]) - \
                        set([index_1, index_2, index_3]):
                    all_candidates |= layer._candidates[index]

                twin_candidates_valids = set()
                for twin_candidate in twins_candidates:
                    if twin_candidate not in all_candidates:
                        twin_candidates_valids.add(twin_candidate)

                if not twin_candidates_valids:
                    continue

                line_other_indexes = INDEX_REGIONS[index_1]['row']
                line_other_indexes = (set(REGION_INDEXES['row'][i])
                                      - set([index_1, index_2, index_3]))
                layer_has_changed = False
                for index in line_other_indexes:
                    if twin_candidates_valids & layer._candidates[index]:
                        layer_has_changed = True
                        layer._candidates[index] = (layer._candidates[index]
                                                    - twin_candidates_valids)

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

                twins_candidates = set()
                if index_1_candidates & index_2_candidates:
                    twins_candidates |= index_1_candidates & index_2_candidates
                if index_2_candidates & index_3_candidates:
                    twins_candidates |= index_2_candidates & index_3_candidates
                if index_1_candidates & index_3_candidates:
                    twins_candidates |= index_1_candidates & index_3_candidates

                offset += BLOCK_WIDTH * GRID_WIDTH

                if not twins_candidates:
                    continue

                all_candidates = set()
                block_index = INDEX_REGIONS[index_1]['block']
                for index in set(REGION_INDEXES['block'][block_index]) - \
                        set([index_1, index_2, index_3]):
                    all_candidates |= layer._candidates[index]

                twin_candidates_valids = set()
                for twin_candidate in twins_candidates:
                    if twin_candidate not in all_candidates:
                        twin_candidates_valids.add(twin_candidate)

                if not twin_candidates_valids:
                    continue

                line_other_indexes = INDEX_REGIONS[index_1]['col']
                line_other_indexes = (set(REGION_INDEXES['col'][i])
                                      - set([index_1, index_2, index_3]))
                layer_has_changed = False
                for index in line_other_indexes:
                    if twin_candidates_valids & layer._candidates[index]:
                        layer_has_changed = True
                        layer._candidates[index] = (layer._candidates[index]
                                                    - twin_candidates_valids)

                if layer_has_changed:
                    return layer
