import unittest
from unittest.mock import Mock
from src.utils.linefeeder import LineFeeder
import os

class TestLineFeedr(unittest.TestCase):

    def setUp(self):
        self._filename = "line_feeder_unittest_file.txt"
        file = open(self._filename, 'w')
        file.write("al\n")
        file.write("kfalamilskdfsankdj\n")
        file.write("a\n")
        file.write("lasdjlsadflsakmfl\n")
        file.write("\n")
        file.write("dkasfslamilaldnlsakdnasld\n")
        file.write("kafjdfnsakjlndsalam\n")
        file.write("ildsa\n")
        file.write("\n")
        file.write("lamil\n")
        file.write("kfajjfhaskdfsalami\n")
        file.write("aldnksand\n")
        file.close()

        self._algorithm = Mock()

    def tearDown(self):
        os.remove(self._filename)

    def test_no_match(self):
        self._algorithm.get_pattern = Mock(return_value = "aaaaa")
        self._algorithm.get_results = Mock(return_value = [])
        lf = LineFeeder(self._algorithm, self._filename)
        self.assertEqual([], lf.get_results())

    def test_match(self):
        self._algorithm.get_pattern = Mock(return_value = "lamil")
        self._algorithm.get_results = Mock(side_effect = [[5], [], [], [10], [], [], [4], [], []])
        lf = LineFeeder(self._algorithm, self._filename)
        self.assertEqual([5, 44, 87], lf.get_results())

    def test_match_letter(self):
        self._algorithm.get_pattern = Mock(return_value = "l")
        self._algorithm.get_results = Mock(side_effect = [[1], [3, 7], [], [0, 5, 10, 16], [6, 10, 12, 15, 23], [11, 16], [1], [0,4], [14], [1]])
        lf = LineFeeder(self._algorithm, self._filename)
        self.assertEqual([1,5,9,21,26,31,37,44,48,50,53,61,74,79,83,87,91,106,111], lf.get_results())


if __name__ == '__main__':
    unittest.main()
