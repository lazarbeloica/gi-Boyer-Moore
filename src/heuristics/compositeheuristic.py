from src.heuristics.heuristic import Heuristic

class CompositeHeuristic(Heuristic):

    def __init__(self, heur_list):
        self._heuristics = set()
        for heur in heur_list:
            self.add(heur)

    def preprocess(self, pattern):
        '''
        Does the pattern preprocessing requred for all the heuristics it contains.

        :param str pattern: The pattern that is used.
        '''
        for heuristic in self.get_heuristics():
            heuristic.preprocess(pattern)

    def add(self, heuristic):
        '''
        Adds a new heuristic to the composition.

        :param heuristics.Heuristic heuristic: A heuristic to be added.
        '''
        self._heuristics.add(heuristic)

    def get_heuristics(self):
        return self._heuristics

    def remove(self, heuristic):
        '''
        Removes specific hheuristic from the set of heuristics used.

        :param heuristics.Heuristic heuristic: A heuristic to be removed from the set.
        '''
        self._heuristics.discard(heuristic)

    def get_shift_pattern_not_found(self, **kwargs):
        '''
        Returns the maximum shift found by running all the heuristics in the set when the pattern is not found.
        Input depends on the input necessary for all the heuristics in the set.
        '''
        return max([heuristic.get_shift_pattern_not_found(**kwargs) for heuristic in self.get_heuristics()])

    def get_shift_pattern_found(self, **kwargs):
        '''
        Returns the maximum shift found by running all the heuristics in the set when the pattern is found.
        Input depends on the input necessary for all the heuristics in the set.
        '''
        return max([heuristic.get_shift_pattern_found(**kwargs) for heuristic in self.get_heuristics()])
    
    def get_name(self):
        return " + ".join([heuristic.get_name() for heuristic in self.get_heuristics()])
