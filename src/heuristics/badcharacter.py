from src.heuristics.heuristic import Heuristic, NUMBER_OF_CHARACTERS

class BadCharacter(Heuristic):

    def preprocess(self, pattern_):
        self._bad_chars = [-1] * NUMBER_OF_CHARACTERS
        self._pattern_len = len(pattern_)
        for i in range(self._pattern_len):
            self._bad_chars[ord(pattern_[i])] = i

    def _get_bad_chars(self):
        return self._bad_chars

    def get_shift_pattern_found(self, **kwargs):
        text = kwargs['text']
        text_len = kwargs['text_len']
        shift = kwargs['shift']
        return (text_len - self._get_bad_chars()[ord(text[shift + text_len])] if shift + text_len < self._pattern_len else 1)

    def get_shift_pattern_not_found(self, **kwargs):
        index = kwargs['index']
        text = kwargs['text']
        shift = kwargs['shift']
        return max(1 , index - self._get_bad_chars()[ord(text[shift + index])])