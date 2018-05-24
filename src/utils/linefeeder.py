
class LineFeeder():
    '''
    Utils class for interacting with files and
    feeding the lines to the algorithm
    '''
    
    def __init__(self, algorithm=None, file_path = None):
        '''
        :optonal param file_path_: Full path to a file you wish to search
        :param algorithm:         Algorithm, with already set parameters, you wish to be used       
        '''
        self.set_algorithm(algorithm)

        self.set_file_path(file_path)
    
    
    def set_file_path(self, file_path):
            self._file_path = file_path

    def get_file_path(self):
            return self._file_path
        
    def set_algorithm(self, algorithm):
            self._algorithm = algorithm

    def get_algorithm(self):
            return self._algorithm

    def search_yield(self, algorithm=None, file_path = None):
        '''
        Searches for the given pattern in the given file using given algorithm.
        
        '''
        if self.get_algorithm() is None and algorithm is None:
            raise Exception('Algorithm must be set')
        
        if self.get_file_path() is None and file_path is None:
            raise Exception('file_path must be set')
        
        if file_path is not None:
            self.set_file_path(file_path)
            
        if algorithm is not None:
            self.set_algorithm(algorithm)

        pattern_len = len(self.get_algorithm().get_pattern())
        global_shift = 0
        line = ""

        with open(self.get_file_path()) as file:
            for new_line in file:
                new_line = new_line.strip('\n')
                new_line = new_line.strip('\r')
                line += new_line
                if (len(line) < pattern_len or new_line == ''):
                    continue
    
                self.get_algorithm().set_text(line)
                for el in self.get_algorithm().get_results():
                    yield (el + global_shift)
    
                global_shift += len(line) - pattern_len + 1
                if pattern_len == 1:
                    line = ""
                else:
                    line = line[(-1 * pattern_len + 1):]
                    
                    
    def get_results(self, algorithm=None, file_path = None):
        return sorted([res for res in self.search_yield(algorithm, file_path)])    