"""BlockBlock Preprocessor for sudokulib"""
from sudokulib.constants import BLOCK_WIDTH
from sudokulib.constants import REGION_INDEXES
from sudokulib.preprocessors import BasePreprocessor


class BlockBlockPreprocessor(BasePreprocessor):
    """Block/Block Interaction preprocessor"""
    name = 'Block Block Interaction'

    def get_all_candidates(self, layer, indexes):
        """Retrieve all candidates for a list of indexes"""
        common_candidates = set()
        for index in indexes:
            candidates = layer._candidates[index]
            if candidates:
                common_candidates |= candidates

        return common_candidates

    def clean(self, layer, candidate,
              line_indexes_1, line_indexes_2,
              start, end):
        """Remove the candidate in the layer"""
        candidate_to_remove = set([candidate])
        for index in line_indexes_1[start:end] + line_indexes_2[start:end]:
            layer._candidates[index] = layer._candidates[index] - \
                                       candidate_to_remove
        return layer

    def eliminate(self, layer, combination,
                  line_indexes_1, line_indexes_2,
                  block_1, block_2, block_3):
        """Clean the layer of matching combination"""
        for candidate in combination - (block_1 | block_2):
            return self.clean(layer, candidate,
                              line_indexes_1, line_indexes_2,
                              6, 9)
        for candidate in combination - (block_1 | block_3):
            return self.clean(layer, candidate,
                              line_indexes_1, line_indexes_2,
                              3, 6)
        for candidate in combination - (block_2 | block_3):
            return self.clean(layer, candidate,
                              line_indexes_1, line_indexes_2,
                              0, 3)

    def _preprocess(self, layer):
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

                line_sum = (int(bool(line_1_common))
                            + int(bool(line_2_common))
                            + int(bool(line_3_common)))
                if line_sum == 1:
                    # We can pass to the next iteration
                    continue

                combin_1 = line_1_common & line_2_common
                combin_2 = line_2_common & line_3_common
                combin_3 = line_1_common & line_3_common

                if combin_1:
                    new_layer = self.eliminate(
                        layer, combin_1,
                        line_1_indexes, line_2_indexes,
                        line_3_bloc_1, line_3_bloc_2, line_3_bloc_3)
                    if new_layer:
                        return new_layer

                if combin_2:
                    new_layer = self.eliminate(
                        layer, combin_2,
                        line_2_indexes, line_3_indexes,
                        line_1_bloc_1, line_1_bloc_2, line_1_bloc_3)
                    if new_layer:
                        return new_layer

                if combin_3:
                    new_layer = self.eliminate(
                        layer, combin_3,
                        line_1_indexes, line_3_indexes,
                        line_2_bloc_1, line_2_bloc_2, line_2_bloc_3)
                    if new_layer:
                        return new_layer
