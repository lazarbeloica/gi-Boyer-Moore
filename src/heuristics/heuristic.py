from abc import ABC, abstractmethod

NUMBER_OF_CHARACTERS = 256 #number of characters in alphabet

class Heuristic(ABC):

    def __init__(self, pattern_):
        self.set_pattern(pattern_)
        
    def set_pattern(self, pattern):
        self._pattern = pattern
        
    def get_pattern(self):
        return self._pattern

    @abstractmethod
    def get_shift_pattern_found(self, **kwargs): 
        pass

    @abstractmethod
    def get_shift_pattern_not_found(self, **kwargs): 
        pass

    @abstractmethod
    def preprocess(self):
        pass
    