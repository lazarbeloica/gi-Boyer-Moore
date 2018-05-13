from abc import ABC, abstractmethod

NUMBER_OF_CHARACTERS = 256 #number of characters in alphabet

class Heuristic(ABC):

    @abstractmethod
    def get_shift_pattern_found(self, **kwargs):
        pass

    @abstractmethod
    def get_shift_pattern_not_found(self, **kwargs):
        pass

    @abstractmethod
    def preprocess(self, pattern_):
        pass
