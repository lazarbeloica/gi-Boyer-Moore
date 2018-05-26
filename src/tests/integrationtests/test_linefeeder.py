import unittest
import os
from src.algorithm.boyermoore import BoyerMoore
from src.utils.linefeeder import LineFeeder

class TestLineFeeder(unittest.TestCase):
    '''
    This is a base class, it will not be used for testing, subclasses of this class will be used.
    '''

    def setUp(self):
        self.skipTest("Not used for testing")

    def set_heuristic(self, heuristic_):
        self._heuristic = heuristic_

    def _get_heuristic(self):
        return self._heuristic

    def test_find_single_match(self):
        _filename = "line_feeder_integrationtest_file.txt"
        file = open(_filename, 'w')
        file.write("asdjasd\nvhajsdv\najsdbh\nasjd\n asdbha sjasdjasv\nbdjas")
        file.close()

        pattern = "jasdj"
        algorithm = BoyerMoore(self._get_heuristic(), pattern)
        lf = LineFeeder(algorithm, _filename)
        res = lf.get_results()
        self.assertEqual(res, [33])
        os.remove(_filename)

    def test_find_no_match(self):
        _filename = "line_feeder_integrationtest_file.txt"
        file = open(_filename, 'w')
        file.write("asdjasdvh\najsdv\najsd\nbhas\nj\nd asdbha sjas\ndjasvbd\njas")
        file.close()

        pattern = "asff"
        algorithm = BoyerMoore(self._get_heuristic(), pattern)
        lf = LineFeeder(algorithm, _filename)
        res = lf.get_results()
        self.assertEqual(res, [])
        os.remove(_filename)

    def test_more_match(self):
        _filename = "line_feeder_integrationtest_file.txt"
        file = open(_filename, 'w')
        file.write("\nasaj\nakvhajsdajakvvajsd\nbajakvhas\njd asajakvdbha sjasdjaja\nkvasvbd\njas\n\n\n")
        file.close()

        pattern = "ajakv"
        algorithm = BoyerMoore(self._get_heuristic(), pattern)
        lf = LineFeeder(algorithm, _filename)
        res = lf.get_results()
        self.assertEqual(res, [2,12, 23,36,52])
        os.remove(_filename)

    def test_all_match(self):
        _filename = "line_feeder_integrationtest_file.txt"
        file = open(_filename, 'w')
        file.write("aaa\naaa\naa\na")
        file.close()

        pattern = "aa"
        algorithm = BoyerMoore(self._get_heuristic(), pattern)
        lf = LineFeeder(algorithm, _filename)
        res = lf.get_results()
        self.assertEqual(res, [0,1,2,3,4,5,6,7])
        os.remove(_filename)


    def test_single_letter(self):
        _filename = "line_feeder_integrationtest_file.txt"
        file = open(_filename, 'w')
        file.write("aa\naa\naaa\naa")
        file.close()

        pattern = "a"
        algorithm = BoyerMoore(self._get_heuristic(), pattern)
        lf = LineFeeder(algorithm, _filename)
        res = lf.get_results()
        self.assertEqual(res, [0,1,2,3,4,5,6,7,8])
        os.remove(_filename)

    def test_change_pattern(self):
        _filename = "line_feeder_integrationtest_file.txt"
        file = open(_filename, 'w')
        file.write("aaaa\n\naa\naaa")
        file.close()

        pattern = "a"
        algorithm = BoyerMoore(self._get_heuristic(), pattern)
        lf = LineFeeder(algorithm, _filename)
        res = lf.get_results()
        self.assertEqual(res, [0,1,2,3,4,5,6,7,8])
        pattern = "aa"
        algorithm.set_pattern(pattern)
        lf = LineFeeder(algorithm, _filename)
        res = lf.get_results()
        self.assertEqual(res, [0,1,2,3,4,5,6,7])
        os.remove(_filename)

