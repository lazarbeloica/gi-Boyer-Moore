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
        res = self.heuristics.get_shift_pattern_not_found(text=_get_text(), index=2, shift=0)
        self.assertEqual(res,2)

    def test_shift_not_found_1(self):
        '''
        aacaaaacaabaaaaaa
        ****cbba
               ^
        '''
        res = self.heuristics.get_shift_pattern_not_found(text=_get_text(), index=3, shift=4)
        self.assertEqual(res,3)

    def test_shift_not_found_2(self):
        '''
        aacaaaacaabaaaaaa
        **********cbba
                    ^
        '''
        res = self.heuristics.get_shift_pattern_not_found(text=_get_text(), index=2, shift=10)
        self.assertEqual(res,3)

    def test_shift_not_found_3(self):
        '''
        aacaaaacaabaaaaaa
        *************cbba
                       ^
        '''
        res = self.heuristics.get_shift_pattern_not_found(text=_get_text(), index=2, shift=13)
        self.assertEqual(res,3)

    def test_shift_not_found_4(self):
        '''
        cbbxaacaaaacaabaa
        cbba
           ^
        '''
        text = "cbbxaacaaaacaabaa"
        res = self.heuristics.get_shift_pattern_not_found(text=text, index=3, shift=0)
        self.assertEqual(res,4)

    def test_shift_found_0(self):
        '''
        cbbacacaabaaaaaa
        cbba
        ****cbba  <- resulting
        '''
        text = "cbbacacaabaaaaaa"
        res = self.heuristics.get_shift_pattern_found(text=text, text_len=len(text) , shift=0)
        self.assertEqual(res,4)

    def test_shift_found_1(self):
        '''
        cbbabacaabaaaaaa
        cbba
        **cbba    <- resulting
        '''
        text = "cbbabacaabaaaaaa"
        res = self.heuristics.get_shift_pattern_found(text=text, text_len=len(text) , shift=0)
        self.assertEqual(res,2)

    def test_shift_found_2(self):
        '''
        cbbaxacaabaaaaaa
        cbba
        **** cbba   <- resulting
        '''
        text = "cbbaxacaabaaaaaa"
        res = self.heuristics.get_shift_pattern_found(text=text, text_len=len(text) , shift=0)
        self.assertEqual(res,5)

    def test_shift_found_3(self):
        '''
        cbbaxacaabaacbbac
        ************cbba
        ****cbba    <- resulting
        '''
        text = "cbbaxacaabaaaaaa"
        res = self.heuristics.get_shift_pattern_found(text=text, text_len=len(text) , shift=12)
        self.assertEqual(res,1)


if __name__ == '__main__':
    unittest.main()
