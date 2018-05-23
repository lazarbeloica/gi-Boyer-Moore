import unittest
from src.heuristics.heuristic import Heuristic
from src.heuristics.secondheuristic import SecndHeuristic

class TestBadCharacterHeurisics(unittest.TestCase):

    def setUp(self):
        self.heuristics = SecndHeuristic()
        self.pattern = "cbba"
        self.heuristics.preprocess(self.pattern)

############ missmatch on chr which is in the end ###############

    def test_shift_not_found_0(self):
        '''
        aacaaaacaabaaaaaa
        cbba
           ^
        *cbba        <- resulting
        '''
        text = "aacaaaacaabaaaaaa"
        index = 3
        res = self.heuristics.get_shift_pattern_not_found(next_letter=text[index + 1], next_next_letter=text[index + 2], index=index)
        self.assertEqual(res,1)

    def test_shift_not_found_1(self):
        '''
        aacaacacaabaaaaaa
        cbba
           ^
        *cbba    <- resulting
        '''
        text = "aacaacacaabaaaaaa"
        index = 3
        res = self.heuristics.get_shift_pattern_not_found(next_letter=text[index + 1], next_next_letter=text[index + 2], index=index)
        self.assertEqual(res,1)

    def test_shift_not_found_2(self):
        '''
        aacacaacaabaaaaaa
        cbba
           ^
        ****cbba    <- resulting
        '''
        text = "aacacaacaabaaaaaa"
        index = 3
        res = self.heuristics.get_shift_pattern_not_found(next_letter=text[index + 1], next_next_letter=text[index + 2], index=index)
        self.assertEqual(res,4)

    def test_shift_not_found_3(self):
        '''
        aacaccacaabaaaaaa
        cbba
           ^
        *****cbba    <- resulting
        '''
        text = "aacaccacaabaaaaaa"
        index = 3
        res = self.heuristics.get_shift_pattern_not_found(next_letter=text[index + 1], next_next_letter=text[index + 2], index=index)
        self.assertEqual(res,5)

    def test_shift_not_found_4(self):
        '''
        aacacbacaabaaaaaa
        cbba
           ^
        ****cbba       <- resulting
        '''
        text = "aacacbacaabaaaaaa"
        index = 3
        res = self.heuristics.get_shift_pattern_not_found(next_letter=text[index + 1], next_next_letter=text[index + 2], index=index)
        self.assertEqual(res,4)

############ missmatch on chr which is not in the end ###############

    def test_shift_not_found_5(self):
        '''
        aabaaaacaabaaaaaa
        cbba
         ^
        *cbba         <- resulting
        '''
        text = "aabaaaacaabaaaaaa"
        index = 1
        res = self.heuristics.get_shift_pattern_not_found(next_letter=text[index + 1], next_next_letter=text[index + 2], index = index)
        self.assertEqual(res,1)

    def test_shift_not_found_6(self):
        '''
        aacabcacaabaaaaaa
        cbba
          ^
        *****cbba    <- resulting
        '''
        text = "aacabcacaabaaaaaa"
        index = 2
        res = self.heuristics.get_shift_pattern_not_found(next_letter=text[index + 1], next_next_letter=text[index + 2], index = index)
        self.assertEqual(res,5)

    def test_shift_not_found_7(self):
        '''
        aacaxxacaabaaaaaa
        cbba
          ^
        ******cbba    <- resulting
        '''
        text = "aacaxxacaabaaaaaa"
        index = 2
        res = self.heuristics.get_shift_pattern_not_found(next_letter=text[index + 1], next_next_letter=text[index + 2], index = index)
        self.assertEqual(res,6)

    def test_shift_not_found_8(self):
        '''
        aacabcacaabaaaaaa
        cbba
          ^
        **cbba       <- resulting
        '''
        text = "aacabcacaabaaaaaa"
        index = 2
        res = self.heuristics.get_shift_pattern_not_found(next_letter=text[index + 1], next_next_letter=text[index + 2], index = index)
        self.assertEqual(res,2)

    def test_shift_found_0(self):
        '''
        cbbacacaabaaaaaa
        cbba
        ****cbba  <- resulting
        '''
        text = "cbbacacaabaaaaaa"
        res = self.heuristics.get_shift_pattern_found(next_letter=text[4], next_next_letter=text[5])
        self.assertEqual(res,4)

    def test_shift_found_1(self):
        '''
        cbbabacaabaaaaaa
        cbba
        **cbba    <- resulting
        '''
        text = "cbbabacaabaaaaaa"
        res = self.heuristics.get_shift_pattern_found(next_letter=text[4], next_next_letter=text[5])
        self.assertEqual(res,2)

    def test_shift_found_2(self):
        '''
        cbbaxacaabaaaaaa
        cbba
        *****cbba   <- resulting
        '''
        text = "cbbaxacaabaaaaaa"
        res = self.heuristics.get_shift_pattern_found(next_letter=text[4], next_next_letter=text[5])
        self.assertEqual(res,5)

    def test_shift_found_3(self):
        '''
        cbbaxxcaabaaaaaa
        cbba
        ******cbba   <- resulting
        '''
        text = "cbbaxxcaabaaaaaa"
        res = self.heuristics.get_shift_pattern_found(next_letter=text[4], next_next_letter=text[5])
        self.assertEqual(res,6)

    def test_shift_found_4(self):
        '''
        cbbaababaaaaaa
        cbba
        *cbba   <- resulting
        '''
        text = "cbbaababaaaaaa"
        res = self.heuristics.get_shift_pattern_found(next_letter=text[4], next_next_letter=text[5])
        self.assertEqual(res,1)

    def test_shift_found_5(self):
        '''
        cbbabbabaaaaaa
        cbba
        ***cbba   <- resulting
        '''
        text = "cbbabbabaaaaaa"
        res = self.heuristics.get_shift_pattern_found(next_letter=text[4], next_next_letter=text[5])
        self.assertEqual(res,3)


if __name__ == '__main__':
    unittest.main()
