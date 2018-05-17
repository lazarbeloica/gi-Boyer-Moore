from src.heuristics.heuristic import Heuristic, NUMBER_OF_CHARACTERS

class GoodSuffix(Heuristic):

    def _set_occ_array(self, occ_array):
        self._occ_array = occ_array

    def _get_occ_array(self):
        return self._occ_array

    def _set_shift_array(self, shift_array):
        self._shift_array = shift_array

    def _get_shift_array(self):
        return self._shift_array

    @staticmethod
    def preprocess_first_case(pattern_, shift_array, bpos):
        m = len(pattern_)
        i = m
        j = m + 1
        bpos[i] = j
        while i>0:
            while(j<=m and pattern_[i-1] != pattern_[j-1]):
                if shift_array[j] == 0:
                    shift_array[j] = j-i
                j = bpos[j]
            i-= 1
            j-= 1
            bpos[i] = j

    @staticmethod
    def create_occ_array(pattern_):
        occ_array = [-1] * NUMBER_OF_CHARACTERS
        for i in range(len(pattern_)):
            occ_array[ord(pattern_[i])] = i
        return occ_array

    @staticmethod
    def preprocess_second_case(pattern_, shift_array, bpos):
        j = bpos[0]
        m = len(pattern_)
        for i in range(m+1):
            if shift_array[i] == 0:
                shift_array[i] = j
            if i == j:
                j = bpos[j]


    def preprocess(self, pattern_):
        self._set_occ_array(GoodSuffix.create_occ_array(pattern_))
        m = len(pattern_)
        bpos_temp = [0] * (m + 1)
        shift_array_temp = [0] * (m + 1)
        GoodSuffix.preprocess_first_case(pattern_, shift_array_temp, bpos_temp)
        GoodSuffix.preprocess_second_case(pattern_, shift_array_temp, bpos_temp)
        self._set_shift_array(shift_array_temp)



    def get_shift_pattern_found(self, **kwargs):
        return self._get_shift_array()[0]


    def get_shift_pattern_not_found(self, **kwargs):
        cur_letter = kwargs['cur_letter']
        index = kwargs['index']
        return max(self._get_shift_array()[index+1], index - self._get_occ_array()[ord(cur_letter)])

