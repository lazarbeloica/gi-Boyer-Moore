from src.heuristics.badcharacter import BadCharacter
from src.algorithm.boyermoore import BoyerMoore
'''
Boyer Moore Hosrpool only uses the bad character shift. In BMH argorithm, no matter 
the location of mismatching, the distance of shift to right is determined by the 
character in the text string which is aligned to the last one of pattern string
'''

class FirstHeuristic(BadCharacter):
    
    def preprocess(self, pattern_):
        self._bad_chars_not_found = {}  
        self._pattern_len = len(pattern_)
        for i in range(self._pattern_len - 1): # last char is not used for preprocessing
            self._bad_chars_not_found[pattern_[i]] = self._pattern_len - i - 1
            
        BadCharacter.preprocess(self, pattern_)
        
    def get_name(self):
        return 'First heuristic'
    
    def get_shift_pattern_not_found(self, **kwargs):
        aligned_letter = kwargs['aligned_letter']
        return self._bad_chars_not_found.get(aligned_letter, self._pattern_len)