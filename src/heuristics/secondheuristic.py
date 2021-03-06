from src.heuristics.heuristic import Heuristic

class SecndHeuristic(Heuristic):

    def preprocess(self, pattern_):
        '''
        Does the preprocessing on pattern required for the
        badcharacter heuristics.

        :param str pattern: Pattern we are searching for
        '''
        self._bad_chars = {}
        self._bad_chr_cnt = {}
        self._pattern_len = len(pattern_)
        self._pattern = pattern_

        for i in range(self._pattern_len):
            self._bad_chars[pattern_[i]] = i
            self._bad_chr_cnt[pattern_[i]] = self._bad_chr_cnt.get(pattern_[i], 0) + 1

    def _calculate_skip(self, letter):
        if letter not in self._bad_chars:
            return self._pattern_len + 1

        return self._pattern_len - self._bad_chars[letter]

    def _calculate_skip2(self, letter):
        if letter is None:
            return -1
        return self._calculate_skip(letter) + 1

    def _occurs_in_pattern(self, letter):
        return self._bad_chars.get(letter, 0)

    def get_shift_pattern_found(self, **kwargs):
        '''
        Shift the pattern so that the bad character in text
        aligns with the last occurrence of it in pattern.

        :NOTE: This heuristic is agnostic of the textlen, it is up to the caller to
                    check if the shift could be made

        :param char next_letter:        Next letter after the end of the part of the text we are comparing pattern against
        :param char next_next_letter:   Second letter after the end of the part of the text we are comparing pattern against
        :returns integer:               The value of the next shift, 0 if bad parameters were passed.
        '''
        next_letter = kwargs['next_letter']
        next_next_letter = kwargs['next_next_letter']

        return (1 if self._calculate_skip(next_letter) == 1 \
            else max(self._calculate_skip(next_letter),
                     self._calculate_skip2(next_next_letter)))

    def get_shift_pattern_not_found(self, **kwargs):
        '''
        Shift the pattern so that the bad character in text
        aligns with the last occurrence of it in pattern.

        :NOTE: This heuristic is agnostic of the textlen, it is up to the caller to
                    check if the shift could be made

        :param char next_letter:        Next letter after the end of the part of the text we are comparing pattern against
        :param char next_next_letter:   Second letter after the end of the part of the text we are comparing pattern against
        :param integer index:           Current index of the pattern being checked
        :returns integer:               The value of the next shift, 0 if bad parameters were passed.
        '''
        next_letter = kwargs['next_letter']
        next_next_letter = kwargs['next_next_letter']
        index = kwargs['index']

        if index == self._pattern_len - 1:
            #missmach happend at the last pattern chr
            return (1 if self._calculate_skip(next_letter) == 1 \
            else max(self._calculate_skip(next_letter),
                     self._calculate_skip2(next_next_letter)))
        else:
            if self._calculate_skip(next_letter) == 1 \
            and self._occurs_in_pattern(self._pattern[index]) == 1:
                return max(self._pattern_len + 1, self._calculate_skip2(next_next_letter))

            return max(self._calculate_skip(next_letter),
                           self._calculate_skip2(next_next_letter))

    def get_name(self):
        return "Imporved BMHS"