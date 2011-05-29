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


class BlockBlockPreprocessor(BasePreprocessor):
    """Block/Block Interaction preprocessor"""
    name = 'Block Block Interaction'

    def get_all_candidates(self, layer, indexes):
        common_candidates = set()
        for index in indexes:
            candidates = layer._candidates[index]
            if candidates:
                common_candidates |= layer._candidates[index]

        return common_candidates

    def preprocess(self, layer):
        for region in ('row', 'col'):
            for i in range(BLOCK_WIDTH):
                line_index_1 = i * BLOCK_WIDTH
                line_index_2 = line_index_1 + 1
                line_index_3 = line_index_2 + 1

                line_1_indexes = REGION_INDEXES[region][line_index_1]
                line_2_indexes = REGION_INDEXES[region][line_index_2]
                line_3_indexes = REGION_INDEXES[region][line_index_3]

                line_1_block_1 = self.get_all_candidates(
                    layer, line_1_indexes[0:3])
                line_1_block_2 = self.get_all_candidates(
                    layer, line_1_indexes[3:6])
                line_1_block_3 = self.get_all_candidates(
                    layer, line_1_indexes[6:9])

                line_2_block_1 = self.get_all_candidates(
                    layer, line_2_indexes[0:3])
                line_2_block_2 = self.get_all_candidates(
                    layer, line_2_indexes[3:6])
                line_2_block_3 = self.get_all_candidates(
                    layer, line_2_indexes[6:9])

                line_3_block_1 = self.get_all_candidates(
                    layer, line_3_indexes[0:3])
                line_3_block_2 = self.get_all_candidates(
                    layer, line_3_indexes[3:6])
                line_3_block_3 = self.get_all_candidates(
                    layer, line_3_indexes[6:9])

                line_1_common = line_1_block_1 & line_1_block_2 & line_1_block_3
                line_2_common = line_2_block_1 & line_2_block_2 & line_2_block_3
                line_3_common = line_3_block_1 & line_3_block_2 & line_3_block_3

                combin_1 = line_1_common & line_2_common
                combin_2 = line_2_common & line_3_common
                combin_3 = line_1_common & line_3_common

                if not combin_1 and not combin_2 and not combin_3:
                    # We can pass to the next iteration
                    continue

                if combin_1:
                    # Elemination of commons_candidates in the appropriates cells
                    for potential_candidate in combin_1:
                        if not potential_candidate in line_3_block_1 | line_3_block_2:
                            for index in line_1_indexes[6:9] + line_2_indexes[6:9]:
                                layer._candidates[index] = layer._candidates[index] - \
                                                           set([potential_candidate])
                            return layer
                        if not potential_candidate in line_3_block_1 | line_3_block_3:
                            for index in line_1_indexes[3:6] + line_2_indexes[3:6]:
                                layer._candidates[index] = layer._candidates[index] - \
                                                           set([potential_candidate])
                            return layer
                        if not potential_candidate in line_3_block_2 | line_3_block_3:
                            for index in line_1_indexes[0:3] + line_2_indexes[0:3]:
                                layer._candidates[index] = layer._candidates[index] - \
                                                           set([potential_candidate])
                            return layer
                if combin_2:
                    # Elemination of commons_candidates in the appropriates cells
                    for potential_candidate in combin_2:
                        if not potential_candidate in line_1_block_1 | line_1_block_2:
                            for index in line_2_indexes[6:9] + line_3_indexes[6:9]:
                                layer._candidates[index] = layer._candidates[index] - \
                                                           set([potential_candidate])
                            return layer
                        if not potential_candidate in line_1_block_1 | line_1_block_3:
                            for index in line_2_indexes[3:6] + line_3_indexes[3:6]:
                                layer._candidates[index] = layer._candidates[index] - \
                                                           set([potential_candidate])
                            return layer
                        if not potential_candidate in line_1_block_2 | line_1_block_3:
                            for index in line_2_indexes[0:3] + line_3_indexes[0:3]:
                                layer._candidates[index] = layer._candidates[index] - \
                                                           set([potential_candidate])
                            return layer

                if combin_3:
                    # Elemination of commons_candidates in the appropriates cells
                    for potential_candidate in combin_3:
                        if not potential_candidate in line_2_block_1 | line_2_block_2:
                            for index in line_1_indexes[6:9] + line_3_indexes[6:9]:
                                layer._candidates[index] = layer._candidates[index] - \
                                                           set([potential_candidate])
                            return layer
                        if not potential_candidate in line_2_block_1 | line_2_block_3:
                            for index in line_1_indexes[3:6] + line_3_indexes[3:6]:
                                layer._candidates[index] = layer._candidates[index] - \
                                                           set([potential_candidate])
                            return layer
                        if not potential_candidate in line_2_block_2 | line_2_block_3:
                            for index in line_1_indexes[0:3] + line_3_indexes[0:3]:
                                layer._candidates[index] = layer._candidates[index] - \
                                                           set([potential_candidate])
                            return layer
        return None


class NakedSubsetPreprocessor(BasePreprocessor):
    """NakedSubset preprocessor"""
    name = 'Naked Subset'

    def preprocess(self, layer):
        layer_has_change = False
        for region in ('row', 'col', 'block'):
            for i in range(GRID_WIDTH):
                candidates_indexes = {}
                indexes = REGION_INDEXES[region][i]
                for index in indexes:
                    candidates = layer._candidates[index]
                    candidates = ''.join(sorted(list(candidates)))
                    candidates_indexes.setdefault(candidates, [])
                    candidates_indexes[candidates].append(index)
                for key, item in candidates_indexes.items():
                    key_len = len(key)
                    item_len = len(item)
                    if key_len > 1 and key_len == item_len:
                        for candidate_to_remove in list(key):
                            for index in indexes:
                                if index not in item:
                                    layer_has_change = True
                                    layer._candidates[index] -= set(
                                        candidate_to_remove)
                if layer_has_change:
                    return layer
        return None
