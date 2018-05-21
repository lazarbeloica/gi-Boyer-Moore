from src.algorithm.boyermoore import BoyerMoore

class LineFeeder():
    '''
    Utils class for interacting with files and
    feeding the lines to the algorithm
    '''

    def __init__(self, filename_, algorithm_, pattern_ = None):
        '''
        :param str filename_:           Full path to a file you wish to search
        :param BoyerMoore algorithm_:   Instance of a BoyerMoore class
        :optonal param str pattern_:    Pattern you wish to search for. This will override the pattern
                                            set in the instance of the algorithm_ class. If this argument
                                            is not specified, it pattern needs to be set in the algorithm_.
        '''
        self._alg = algorithm_
        self._file = open(filename_, 'r')
        if pattern_ is not None:
           self._alg.set_pattern(pattern_)
        self._result = []

    def search(self):
        '''
        Searches for the given pattern in the given file using given algorithm.
        '''
        pattern_len = len(self._alg.get_pattern())
        globalShift = 0
        line = ""

        #for new_line in iter(lambda: self._file.getline(), ''):
        for new_line in self._file:
            new_line = new_line.replace('\n', '')
            new_line = new_line.replace('\r', '')
            line += new_line
            if (len(line) < pattern_len or new_line == ''):
                continue

            self._alg.set_text(line)
            res = self._alg.search()
            for el in res:
                self._result.append(el + globalShift)

            globalShift += len(line) - pattern_len + 1
            if pattern_len == 1:
                line = ""
            else:
                line = line[(-1 * pattern_len + 1):]

        self._file.close()
        return self._result
