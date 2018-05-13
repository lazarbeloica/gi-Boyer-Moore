from src.heuristics.heuristic import Heuristic, NUMBER_OF_CHARACTERS

class BadCharacter(Heuristic):

    def preprocess(self, pattern_):
        '''
        Does the preprocessing on pattern required for the
        badcharacter heuristics.

        :param str pattern: Pattern we are searching for
        '''
        self._bad_chars = [-1] * NUMBER_OF_CHARACTERS
        self._pattern_len = len(pattern_)
        for i in range(self._pattern_len):
            self._bad_chars[ord(pattern_[i])] = i

    def _get_bad_chars(self):
        return self._bad_chars

    def get_shift_pattern_found(self, **kwargs):
        '''
        Shift the pattern so that the bad character in text
        aligns with the last occurrence of it in pattern.

        :param text str:          where the pattern is beeing searched
        :param text_len integer:  the size of the text
        :param shift integer:     current shift in the text
        :returns integer:         The value of the next shift
        '''
        text = kwargs['text']
        text_len = kwargs['text_len']
        shift = kwargs['shift']
        return (self._pattern_len - self._get_bad_chars()[ord(text[shift + self._pattern_len])]\
        if shift + self._pattern_len < text_len
        else 1)

    def get_shift_pattern_not_found(self, **kwargs):
        '''
        Shift the pattern so that the bad character in text
        aligns with the last occurrence of it in pattern.

        :param integer index:   current index of the pattern being checked
        :param str text:        where the pattern is beeing searched
        :param integer shift:   current shift in the text
        :returns integer:         The value of the next shift
        '''
        index = kwargs['index']
        text = kwargs['text']
        shift = kwargs['shift']
        new_shift = index - self._get_bad_chars()[ord(text[shift + index])]
        return (new_shift if new_shift > 0 else index + 1)