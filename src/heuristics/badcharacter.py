from src.heuristics.heuristic import Heuristic

class BadCharacter(Heuristic):

    def preprocess(self, pattern):
        '''
        Does the preprocessing on pattern required for the
        badcharacter heuristics.

        :param str pattern: Pattern we are searching for
        '''
        self._bad_chars = {}
        self._pattern_len = len(pattern)
        for i in range(self._pattern_len):
            self._bad_chars[pattern[i]] = i

    def _get_bad_chars(self):
        return self._bad_chars

    def get_shift_pattern_found(self, **kwargs):
        '''
        Shift the pattern so that the bad character in text
        aligns with the last occurrence of it in pattern.

        :NOTE: This heuristic is agnostic of the textlen, it is up to the caller to
                    check if the shift could be made

        :param char next_letter: Letter after last in the text against witch we are comparing
        :returns integer:         The value of the next shift
        '''
        next_letter = kwargs['next_letter']
        return self._pattern_len - self._get_bad_chars().get(next_letter, -1)

    def get_shift_pattern_not_found(self, **kwargs):
        '''
        Shift the pattern so that the bad character in text
        aligns with the last occurrence of it in pattern.

        :NOTE: This heuristic is agnostic of the textlen, it is up to the caller to
                    check if the shift could be made

        :param integer index:   Current index of the pattern being checked
        :param char cur_letter: Current letter in the text against witch we are comparing
        :returns integer:       The value of the next shift
        '''
        index = kwargs['index']
        cur_letter = kwargs['cur_letter']
        new_shift = index - self._get_bad_chars().get(cur_letter, -1)
        return (new_shift if new_shift > 0 else index + 1)

    def get_name(self):
        return "Bad Character"