from heuristics.heuristic import Heuristic, NUMBER_OF_CHARACTERS

class BadCharacter(Heuristic):

    def preprocess(self, pattern_):
        self._bad_chars = [-1]*NUMBER_OF_CHARACTERS
        for i in range(len(pattern_):
            pattern_[ord(pattern_[i])] = i

    def _get_bad_chars(self):
        return self._bad_chars

    def get_shift_pattern_found(self, **kwargs):    #TODO do a doublecheck
        text = kwargs['text']
        text_len = kwargs['text_len']
        shift = kwargs['shift']
        return (text_len - self._get_bad_chars()[ord(text[shift + text_len])] if shift + text_len < len(self.get_pattern()) else 1)

    def get_shift_pattern_not_found(self, **kwargs): #TODO do a doublecheck
        index = kwargs['index']
        text = kwargs['text']
        shift = kwargs['shift']
        return max(1 , index - self._get_bad_chars()[ord(text[shift + index])])