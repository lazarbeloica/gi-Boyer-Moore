import unittest
from src.heuristics.heuristic import Heuristic
from src.heuristics.goodsuffix import GoodSuffix

class TestGoodSuffixHeurisics(unittest.TestCase):

    def setUp(self):
        self.heuristics = GoodSuffix()
        self.pattern = "cbba"
        self.heuristics.preprocess(self.pattern)

    def test_shift_not_found_0(self):
        '''
        aacaaaacaabaaaaaa
        cbba
          ^
        ****cbba
        '''
        text = "aacaaaacaabaaaaaa"
        res = self.heuristics.get_shift_pattern_not_found(cur_letter=text[2], index=2)
        self.assertEqual(res,4)

    def test_shift_not_found_1(self):
        '''
        aacaaaacaabaaaaaa
        ****cbba
               ^
        *******cbba
        '''
        text = "aacaaaacaabaaaaaa"
        res = self.heuristics.get_shift_pattern_not_found(cur_letter=text[7], index=3)
        self.assertEqual(res,3)

    def test_shift_not_found_2(self):
        '''
        aacaaaacaababaaaa
        **************cbba
                   ^
        '''
        text = "aacaaaacaababaaaa"
        res = self.heuristics.get_shift_pattern_not_found(cur_letter=text[12], index=2)
        self.assertEqual(res,4)

    def test_shift_not_found_3(self):
        '''
        aacaaaacaabaaaaba
        *************cbba
                      ^
        *****************cbba
        '''
        text = "aacaaaacaabaaaaba"
        res = self.heuristics.get_shift_pattern_not_found(cur_letter=text[15], index=2)
        self.assertEqual(res,4)

    def test_shift_not_found_4(self):
        '''
        abbaaacaaaacaabaa
        cbba
        ^
        ****cbba
        '''
        text = "abbaaacaaaacaabaa"
        res = self.heuristics.get_shift_pattern_not_found(cur_letter=text[0], index=0)
        self.assertEqual(res,4)

    def test_shift_not_found_5(self):
        '''
        abbaaacaaaacaabaa
        baba
         ^
        **baba
        '''
        text = "abbaaacaaaacaabaa"
        self.heuristics.preprocess('baba')
        index=1
        res = self.heuristics.get_shift_pattern_not_found(cur_letter=text[index], index = index)
        self.assertEqual(res,2)

    def test_shift_not_found_6(self):
        '''
        baaaaaaaaaaaaaaaaaaaaa
        a
        ^
        *a
        '''
        text = "baaaaaaaaaaaaaaaaaaaaa"
        self.heuristics.preprocess('a')
        index=0
        res = self.heuristics.get_shift_pattern_not_found(cur_letter=text[index], index = index)
        self.assertEqual(res,1)

    def test_shift_not_found_7(self):
        '''
        abaaabababababbabab
        abababab
           ^
        **abababab
        '''
        text = "abaaabababababbabab"
        self.heuristics.preprocess('abababab')
        index=0
        res = self.heuristics.get_shift_pattern_not_found(cur_letter=text[index], index = index)
        self.assertEqual(res,2)


    def test_shift_found_0(self):
        '''
        cbbacacaabaaaaaa
        cbba
        ****cbba  <- resulting
        '''
        text = "cbbacacaabaaaaaa"
        res = self.heuristics.get_shift_pattern_found(next_letter=text[3 + 1])
        self.assertEqual(res,4)

    def test_shift_found_1(self):
        '''
        cbbabacaabaaaaaa
        cbba
        ****cbba    <- resulting
        '''
        text = "cbbabacaabaaaaaa"
        res = self.heuristics.get_shift_pattern_found(next_letter=text[3 + 1])
        self.assertEqual(res,4)

    def test_shift_found_2(self):
        '''
        cbbaxacaabaaaaaa
        cbba
        ****cbba   <- resulting
        '''
        text = "cbbaxacaabaaaaaa"
        res = self.heuristics.get_shift_pattern_found(next_letter=text[3 + 1])
        self.assertEqual(res,4)

    def test_shift_found_3(self):
        '''
        NOTE The caller is responsible to chec the shift
        cbbaxacaabaacbbac
        ************cbba
        ****************cbba    <- resulting
        '''
        text = "cbbaxacaabaacbbac"
        res = self.heuristics.get_shift_pattern_found(next_letter=text[16])
        self.assertEqual(res,4)

    def test_shift_not_found_8(self):
        '''
        abababababababbabab
        abababab
           ^
        **abababab
        '''
        text = "abababababababbabab"
        pattern = 'abababab'
        self.heuristics.preprocess(pattern)
        index=0
        res = self.heuristics.get_shift_pattern_found(next_letter = text[len(pattern)], index = 0)
        self.assertEqual(res,2)


if __name__ == '__main__':
    unittest.main()
