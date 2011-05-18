"""sudokulib grid"""

class Grid(object):
    """Grid of Sudoku"""

    def __init__(self, filename, free_char, mystery_char='X'):
        self.free_char = free_char
        self.mystery_char = mystery_char
        
        self.filename = filename
        source = open(filename, 'r')
        self.data_table = [l.strip() for l in source.readlines()]
        source.close()

        self.height = len(self.data_table)
        self.width = len(self.data_table[0])
        self.check_source()

        self.data = ''.join(self.data_table)
        self.data = self.data.replace(self.free_char, self.mystery_char)        
        

    def check_source(self):
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
            if i and not i % 9:
                string.append('\n%s\n' % ('-' * (self.width * 4)))
            if c == self.mystery_char:
                string.append('| \033[1;31m%s\033[0m ' % c)
            else:
                string.append('| %s ' % c)
            i += 1

        return ''.join(string)
