
class LineFeeder():
    '''
    Utils class for interacting with files and
    feeding the lines to the algorithm
    '''
    
    def __init__(self, algorithm, filename_ = None):
        '''
        :optonal param filename_: Full path to a file you wish to search
        :param algorithm:         Algorithm, with already set parameters, you wish to be used       
        '''
        self._alg = algorithm

        self._set_filename(filename_)
    
    
    def set_filename(self, filename_):
            self._filename = filename_

    def get_filename(self):
            return self._filename
        
    def set_algorithm(self, algorithm):
            self._alg = algorithm

    def get_algorithm(self):
            return self._alg        


    def search_yield(self, filename_ = None):
        '''
        Searches for the given pattern in the given file using given algorithm.
        
        '''
        
        if self._get_filename() is None and filename_ is None:
            raise Exception('Filename must be set')
        
        if filename_ is not None:
            self._set_filename(filename_)

        pattern_len = len(self._get_pattern())
        global_shift = 0
        line = ""

        with open(self._get_filename()) as file:
            for new_line in file:
                new_line = new_line.strip('\n')
                new_line = new_line.strip('\r')
                line += new_line
                if (len(line) < pattern_len or new_line == ''):
                    continue
    
                self._alg.set_text(line)
                for el in self._alg.search_yield():
                    yield (el + global_shift)
    
                global_shift += len(line) - pattern_len + 1
                if pattern_len == 1:
                    line = ""
                else:
                    line = line[(-1 * pattern_len + 1):]
                    
                    
    def get_results(self, filename_ = None):
        return sorted([res for res in self.search_yield(filename_)])

