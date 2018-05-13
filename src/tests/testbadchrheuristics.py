import unittest
from src.heuristics.heuristic import Heuristic
from src.heuristics.badcharacter import BadCharacter
from src.algorithm.boyermoore import BoyerMoore

class BadCharacterTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_find_single_match(self):
        text = "asdjasdvhajsdvajsdbhasjd asdbha sjasdjasvbdjas"
        pattern = "jasdj"
        algorithm = BoyerMoore(BadCharacter(), pattern, text)
        res = algorithm.search()
        self.assertEqual(res, [33])

    def test_find_no_match(self):
        text = "asdjasdvhajsdvajsdbhasjd asdbha sjasdjasvbdjas"
        pattern = "asff"
        algorithm = BoyerMoore(BadCharacter(), pattern, text)
        res = algorithm.search()
        self.assertEqual(res, [])

    def test_more_match(self):
        text = "asajakvhajsdajakvvajsdbajakvhasjd asajakvdbha sjasdjajakvasvbdjas"
        pattern = "ajakv"
        algorithm = BoyerMoore(BadCharacter(), pattern, text)
        res = algorithm.search()
        self.assertEqual(res, [2,12, 23,36,52])

    def test_all_match(self):
        text = "aaaaaaaaa"
        pattern = "aa"
        algorithm = BoyerMoore(BadCharacter(), pattern, text)
        res = algorithm.search()
        self.assertEqual(res, [0,1,2,3,4,5,6,7])

    def test_single_letter(self):
        text = "aaaaaaaaa"
        pattern = "a"
        algorithm = BoyerMoore(BadCharacter(), pattern, text)
        res = algorithm.search()
        self.assertEqual(res, [0,1,2,3,4,5,6,7,8])

    def test_change_pattern(self):
        text = "aaaaaaaaa"
        pattern = "a"
        algorithm = BoyerMoore(BadCharacter(), pattern, text)
        res = algorithm.search()
        self.assertEqual(res, [0,1,2,3,4,5,6,7,8])
        pattern = "aa"
        algorithm.set_pattern(pattern)
        res = algorithm.search()
        self.assertEqual(res, [0,1,2,3,4,5,6,7])

    def test_change_text(self):
        text = "aaaaaaaaa"
        pattern = "a"
        algorithm = BoyerMoore(BadCharacter(), pattern, text)
        res = algorithm.search()
        self.assertEqual(res ,[0,1,2,3,4,5,6,7,8])
        text = "bbbbbbbbbbbbbbb"
        algorithm.set_text(text)
        res = algorithm.search()
        self.assertEqual(res ,[])


if __name__ == '__main__':
    unittest.main()
