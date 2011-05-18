"""sudokulib grid"""
import string

GRID_WIDTH = 9
GRID_TOTAL = 81


class Grid(object):
    """Grid of Sudoku"""

    def __init__(self, filename, free_char, mystery_char='X'):
        self.filename = filename
        self.free_char = free_char
        self.mystery_char = mystery_char

        self.data = self.load_source()

        self.data_solution = ''
        for c in self.data:
            if c == self.mystery_char:
                self.data_solution += self.mystery_char
            else:
                self.data_solution += ' '

    @property
    def missing(self):
        return self.data_solution.count(self.mystery_char)

    @property
    def completed(self):
        return not self.mystery_char in self.data_solution

    def apply_solution(self, index, solution):
        """Apply a solution in the solution data"""
        solution_list = list(self.data_solution)
        solution_list[index] = str(solution)
        self.data_solution = ''.join(solution_list)

    def load_source(self):
        """Load the data from a source"""
        source = open(self.filename, 'r')
        source_data = source.read()
        source.close()

        data = ''
        for c in source_data:
            if c in string.digits + self.free_char:
                if c in ('0', self.free_char):
                    data += self.mystery_char
                else:
                    data += c

        if len(data) != GRID_TOTAL:
            print u'Invalid source file'
            exit(1)

        return data

    def __str__(self):
        string = []
        i = 0
        for c in self.data:
            if i and not i % GRID_WIDTH:
                string.append('\n')
            if i and not i % (GRID_WIDTH * 3):
                string.append('%s\n' % ('-' * (GRID_WIDTH * 3 + 2)))

            if not i % 3 and i % GRID_WIDTH:
                string.append('|')

            if c == self.mystery_char:
                if self.data_solution[i] != self.mystery_char:
                    string.append(' \033[1;32m%s\033[0m ' % \
                                  self.data_solution[i])
                else:
                    string.append(' \033[1;31m%s\033[0m ' % c)
            else:
                string.append(' %s ' % c)
            i += 1

        return ''.join(string)
