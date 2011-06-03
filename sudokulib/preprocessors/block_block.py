"""BlockBlock Preprocessor for sudokulib"""
from sudokulib.constants import BLOCK_WIDTH
from sudokulib.constants import REGION_INDEXES
from sudokulib.preprocessors import BasePreprocessor


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

                line_1_bloc_1 = self.get_all_candidates(
                    layer, line_1_indexes[0:3])
                line_1_bloc_2 = self.get_all_candidates(
                    layer, line_1_indexes[3:6])
                line_1_bloc_3 = self.get_all_candidates(
                    layer, line_1_indexes[6:9])

                line_2_bloc_1 = self.get_all_candidates(
                    layer, line_2_indexes[0:3])
                line_2_bloc_2 = self.get_all_candidates(
                    layer, line_2_indexes[3:6])
                line_2_bloc_3 = self.get_all_candidates(
                    layer, line_2_indexes[6:9])

                line_3_bloc_1 = self.get_all_candidates(
                    layer, line_3_indexes[0:3])
                line_3_bloc_2 = self.get_all_candidates(
                    layer, line_3_indexes[3:6])
                line_3_bloc_3 = self.get_all_candidates(
                    layer, line_3_indexes[6:9])

                line_1_common = line_1_bloc_1 & line_1_bloc_2 & line_1_bloc_3
                line_2_common = line_2_bloc_1 & line_2_bloc_2 & line_2_bloc_3
                line_3_common = line_3_bloc_1 & line_3_bloc_2 & line_3_bloc_3

                combin_1 = line_1_common & line_2_common
                combin_2 = line_2_common & line_3_common
                combin_3 = line_1_common & line_3_common

                if not combin_1 and not combin_2 and not combin_3:
                    # We can pass to the next iteration
                    continue

                if combin_1:
                    # Elemination of common candidates in the other cells
                    for candidate in combin_1:
                        if not candidate in line_3_bloc_1 | line_3_bloc_2:
                            for index in line_1_indexes[6:9] + line_2_indexes[6:9]:
                                layer._candidates[index] = layer._candidates[index] - \
                                                           set([candidate])
                            return layer
                        if not candidate in line_3_bloc_1 | line_3_bloc_3:
                            for index in line_1_indexes[3:6] + line_2_indexes[3:6]:
                                layer._candidates[index] = layer._candidates[index] - \
                                                           set([candidate])
                            return layer
                        if not candidate in line_3_bloc_2 | line_3_bloc_3:
                            for index in line_1_indexes[0:3] + line_2_indexes[0:3]:
                                layer._candidates[index] = layer._candidates[index] - \
                                                           set([candidate])
                            return layer
                if combin_2:
                    # Elemination of common candidates in the other cells
                    for candidate in combin_2:
                        if not candidate in line_1_bloc_1 | line_1_bloc_2:
                            for index in line_2_indexes[6:9] + line_3_indexes[6:9]:
                                layer._candidates[index] = layer._candidates[index] - \
                                                           set([candidate])
                            return layer
                        if not candidate in line_1_bloc_1 | line_1_bloc_3:
                            for index in line_2_indexes[3:6] + line_3_indexes[3:6]:
                                layer._candidates[index] = layer._candidates[index] - \
                                                           set([candidate])
                            return layer
                        if not candidate in line_1_bloc_2 | line_1_bloc_3:
                            for index in line_2_indexes[0:3] + line_3_indexes[0:3]:
                                layer._candidates[index] = layer._candidates[index] - \
                                                           set([candidate])
                            return layer

                if combin_3:
                    # Elemination of common candidates in the other cells
                    for candidate in combin_3:
                        if not candidate in line_2_bloc_1 | line_2_bloc_2:
                            for index in line_1_indexes[6:9] + line_3_indexes[6:9]:
                                layer._candidates[index] = layer._candidates[index] - \
                                                           set([candidate])
                            return layer
                        if not candidate in line_2_bloc_1 | line_2_bloc_3:
                            for index in line_1_indexes[3:6] + line_3_indexes[3:6]:
                                layer._candidates[index] = layer._candidates[index] - \
                                                           set([candidate])
                            return layer
                        if not candidate in line_2_bloc_2 | line_2_bloc_3:
                            for index in line_1_indexes[0:3] + line_3_indexes[0:3]:
                                layer._candidates[index] = layer._candidates[index] - \
                                                           set([candidate])
                            return layer
