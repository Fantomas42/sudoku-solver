"""sudokulib grid"""


class Grid(object):
    """Grid of Sudoku"""

    def __init__(self, filename, free_char, mystery_char='X'):
        self.free_char = free_char
        self.mystery_char = mystery_char

        # Load the datas from a file
        self.filename = filename
        source = open(filename, 'r')
        self.data_table = [l.strip() for l in source.readlines()]
        source.close()

        # Check the source and compute dimensions
        self.height = len(self.data_table)
        self.width = len(self.data_table[0])
        self.check_source()

        # Init the string of data
        self.data = ''.join(self.data_table)
        self.data = self.data.replace(self.free_char, self.mystery_char)

        # Init the string of solution
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

    def check_source(self):
        """Check if the source file is valid"""
        if self.height != self.width:
            print u'Invalid source file'
            exit(1)
        for line in self.data_table:
            if self.width != len(line):
                print u'Invalid source file'
                exit(1)

    def __str__(self):
        string = []
        i = 0
        for c in self.data:
            if i and not i % self.width:
                string.append('\n%s\n' % ('-' * (self.width * 4)))
            if c == self.mystery_char:
                if self.data_solution[i] != self.mystery_char:
                    string.append('| \033[1;32m%s\033[0m ' % \
                                  self.data_solution[i])
                else:
                    string.append('| \033[1;31m%s\033[0m ' % c)
            else:
                string.append('| %s ' % c)
            i += 1

        return ''.join(string)
