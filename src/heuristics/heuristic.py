from abc import ABC, abstractmethod

class Heuristic(ABC):

    @abstractmethod
    def get_shift_pattern_found(self, **kwargs):
        '''
        Calculates the shif of the pattern when the pattern is found in the text.
        '''
        pass

    @abstractmethod
    def get_shift_pattern_not_found(self, **kwargs):
        '''
        Calculates the shif of the pattern when the pattern is not found in the text.
        '''
        pass

    @abstractmethod
    def preprocess(self, pattern_):
        '''
        Does the preprocessing necessary for the heuristics.
        '''
        pass
    
    @abstractmethod
    def get_name(self):
        pass
