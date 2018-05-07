from heuristics.heuristic import Heuristic, NUMBER_OF_CHARACTERS

class BadCharacter(Heuristic):
    

    def preprocess(self):
        self._bad_chars = [-1]*NUMBER_OF_CHARACTERS
        for i in range(len(self.get_pattern())):
            self.get_pattern()[ord(self.get_pattern()[i])] = i

    def _get_bad_chars(self):
        return self._bad_chars
    
    def get_shift_pattern_found(self, **kwargs):    #TODO add implementation
        pass                                    
    
    def get_shift_pattern_not_found(self, **kwargs): #TODO add implementation 
        pass