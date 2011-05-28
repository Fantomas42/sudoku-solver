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
        for i in range(BLOCK_WIDTH):
            line_index_1 = i * BLOCK_WIDTH
            line_index_2 = line_index_1 + 1
            line_index_3 = line_index_2 + 1

            #print line_index_1, line_index_2, line_index_3

            line_1_indexes = REGION_INDEXES['row'][line_index_1]
            line_2_indexes = REGION_INDEXES['row'][line_index_2]
            line_3_indexes = REGION_INDEXES['row'][line_index_3]

            #print line_1_indexes
            #print line_2_indexes
            #print line_3_indexes

            line_1_block_1 = self.get_all_candidates(layer, line_1_indexes[0:3])
            line_1_block_2 = self.get_all_candidates(layer, line_1_indexes[3:6])
            line_1_block_3 = self.get_all_candidates(layer, line_1_indexes[6:9])

            line_2_block_1 = self.get_all_candidates(layer, line_2_indexes[0:3])
            line_2_block_2 = self.get_all_candidates(layer, line_2_indexes[3:6])
            line_2_block_3 = self.get_all_candidates(layer, line_2_indexes[6:9])

            line_3_block_1 = self.get_all_candidates(layer, line_3_indexes[0:3])
            line_3_block_2 = self.get_all_candidates(layer, line_3_indexes[3:6])
            line_3_block_3 = self.get_all_candidates(layer, line_3_indexes[6:9])

            #print line_1_block_1
            #print line_1_block_2
            #print line_1_block_3
            #print line_2_block_1
            #print line_2_block_2
            #print line_2_block_3
            #print line_3_block_1
            #print line_3_block_2
            #print line_3_block_3

            line_1_common_candidates_by_block = line_1_block_1 & line_1_block_2 & line_1_block_3
            line_2_common_candidates_by_block = line_2_block_1 & line_2_block_2 & line_2_block_3
            line_3_common_candidates_by_block = line_3_block_1 & line_3_block_2 & line_3_block_3

            #print 'COMONS 1 : ', line_1_common_candidates_by_block
            #print 'COMONS 2 : ',line_2_common_candidates_by_block
            #print 'COMONS 3 : ',line_3_common_candidates_by_block

            combin_1 = line_1_common_candidates_by_block & line_2_common_candidates_by_block
            combin_2 = line_2_common_candidates_by_block & line_3_common_candidates_by_block
            combin_3 = line_1_common_candidates_by_block & line_3_common_candidates_by_block

            #print 'COMBIN 1 (1, 2)', combin_1
            #print 'COMBIN 2 (2, 3)', combin_2
            #print 'COMBIN 3 (1, 3)', combin_3

            if not combin_1 and not combin_2 and not combin_3:
                # We can pass to the next iteration
                continue

            layer_has_changed = False
            if combin_1:
                #Elemination of commons_candidates in the appropriates cells
                for candidate_to_remove in combin_1 - line_3_common_candidates_by_block:
                    if candidate_to_remove in line_3_block_1:
                        for index in line_1_indexes[0:3] + line_2_indexes[0:3]:
                            layer_has_changed = True
                            layer._candidates[index] = layer._candidates[index] - \
                                                       set([candidate_to_remove])
                    if candidate_to_remove in line_3_block_2:
                        for index in line_1_indexes[3:6] + line_2_indexes[3:6]:
                            layer_has_changed = True
                            layer._candidates[index] = layer._candidates[index] - \
                                                       set([candidate_to_remove])
                    if candidate_to_remove in line_3_block_3:
                        for index in line_1_indexes[6:9] + line_2_indexes[6:9]:
                            layer_has_changed = True
                            layer._candidates[index] = layer._candidates[index] - \
                                                       set([candidate_to_remove])

            if combin_2:
                #Elemination of commons_candidates in the appropriates cells
                for candidate_to_remove in combin_2 - line_1_common_candidates_by_block:
                    if candidate_to_remove in line_1_block_1:
                        for index in line_3_indexes[0:3] + line_2_indexes[0:3]:
                            layer_has_changed = True
                            layer._candidates[index] = layer._candidates[index] - \
                                                       set([candidate_to_remove])
                    if candidate_to_remove in line_1_block_2:
                        for index in line_3_indexes[3:6] + line_2_indexes[3:6]:
                            layer_has_changed = True
                            layer._candidates[index] = layer._candidates[index] - \
                                                       set([candidate_to_remove])
                    if candidate_to_remove in line_1_block_3:
                        for index in line_3_indexes[6:9] + line_2_indexes[6:9]:
                            layer_has_changed = True
                            layer._candidates[index] = layer._candidates[index] - \
                                                       set([candidate_to_remove])

            if combin_3:
                #Elemination of commons_candidates in the appropriates cells
                for candidate_to_remove in combin_3 - line_2_common_candidates_by_block:
                    if candidate_to_remove in line_2_block_1:
                        for index in line_3_indexes[0:3] + line_1_indexes[0:3]:
                            layer_has_changed = True
                            layer._candidates[index] = layer._candidates[index] - \
                                                       set([candidate_to_remove])
                    if candidate_to_remove in line_2_block_2:
                        for index in line_3_indexes[3:6] + line_1_indexes[3:6]:
                            layer_has_changed = True
                            layer._candidates[index] = layer._candidates[index] - \
                                                       set([candidate_to_remove])
                    if candidate_to_remove in line_2_block_3:
                        for index in line_3_indexes[6:9] + line_1_indexes[6:9]:
                            layer_has_changed = True
                            layer._candidates[index] = layer._candidates[index] - \
                                                       set([candidate_to_remove])
            if layer_has_changed:
                return layer

        return None
