from heuristics.heuristic import Heuristic

class CompositeHeuristic(Heuristic):

    def __init__(self, *argv):
        self._heuristics = set()
        for arg in argv:
            self.add(arg)        

    def preprocess(self):
        for heuristic in self.get_heuristics():
            heuristic.preprocess()
            
    def add(self, heuristic):
        self._heuristics.add(heuristic)
        
    def get_heuristics(self):
        return self._heuristics

    def remove(self, heuristic):
        self._heuristics.discard(heuristic)
        
    def get_shift_pattern_not_found(self): 
        return max([heuristic.get_shift_pattern_not_found() for heuristic in self.get_heuristics()]) #TODO double check                                
        
    def get_shift_pattern_found(self): #TODO add implementation
        return max([heuristic.get_shift_pattern_found() for heuristic in self.get_heuristics()]) #TODO double check
    