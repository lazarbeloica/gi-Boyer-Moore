import unittest
from src.heuristics.heuristic import Heuristic
from src.heuristics.badcharacter import BadCharacter

def _get_text():
    return "aacaaaacaabaaaaaa"

class TestBadCharacterHeurisics(unittest.TestCase):

    def setUp(self):
        self.heuristics = BadCharacter()
        self.pattern = "cbba"
        self.text = "aacaaaacaabaaaaaa"
        self.text = len(self.text)
        self.heuristics.preprocess(self.pattern)

    def test_shift_not_found_0(self):
        '''
        aacaaaacaabaaaaaa
        cbba
          ^
        '''
        res = self.heuristics.get_shift_pattern_not_found(cur_letter=_get_text()[2], index=2)
        self.assertEqual(res,2)

    def test_shift_not_found_1(self):
        '''
        aacaaaacaabaaaaaa
        ****cbba
               ^
        '''
        res = self.heuristics.get_shift_pattern_not_found(cur_letter=_get_text()[7], index=3)
        self.assertEqual(res,3)

    def test_shift_not_found_2(self):
        '''
        aacaaaacaabaaaaaa
        **********cbba
                    ^
        '''
        res = self.heuristics.get_shift_pattern_not_found(cur_letter=_get_text()[12], index=2)
        self.assertEqual(res,3)

    def test_shift_not_found_3(self):
        '''
        aacaaaacaabaaaaaa
        *************cbba
                       ^
        '''
        res = self.heuristics.get_shift_pattern_not_found(cur_letter=_get_text()[15], index=2)
        self.assertEqual(res,3)

    def test_shift_not_found_4(self):
        '''
        cbbxaacaaaacaabaa
        cbba
           ^
        '''
        text = "cbbxaacaaaacaabaa"
        res = self.heuristics.get_shift_pattern_not_found(cur_letter=text[3], index=3)
        self.assertEqual(res,4)

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
        **cbba    <- resulting
        '''
        text = "cbbabacaabaaaaaa"
        res = self.heuristics.get_shift_pattern_found(next_letter=text[3 + 1])
        self.assertEqual(res,2)

    def test_shift_found_2(self):
        '''
        cbbaxacaabaaaaaa
        cbba
        **** cbba   <- resulting
        '''
        text = "cbbaxacaabaaaaaa"
        res = self.heuristics.get_shift_pattern_found(next_letter=text[3 + 1])
        self.assertEqual(res,5)

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


if __name__ == '__main__':
    unittest.main()
