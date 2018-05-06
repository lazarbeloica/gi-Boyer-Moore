from abc import ABC, abstractmethod

NUMBER_OF_CHARACTERS = 256 #number of characters in alphabet

class Heuristic(ABC):



    @abstractmethod
    def get_shift_pattern_found(self): #TODO add arguments for this method
        pass

    @abstractmethod
    def get_shift_pattern_not_found(self): #TODO add arguments for this method
        pass

    @abstractmethod
    def preprocess(self):
        pass
    