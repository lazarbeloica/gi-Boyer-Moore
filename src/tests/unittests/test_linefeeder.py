import unittest
from unittest.mock import Mock
from src.utils.linefeeder import LineFeeder
import os

class TestLineFeedr(unittest.TestCase):

    def setUp(self):
        self._filename = "line_feeder_test_file.txt"
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
        self._algorithm.search = Mock(return_value = [])
        lf = LineFeeder(self._filename, self._algorithm)
        self.assertEquals([], lf.search())

    def test_match(self):
        self._algorithm.get_pattern = Mock(return_value = "lamil")
        self._algorithm.search = Mock(side_effect = [[5], [], [], [10], [], [], [4], [], []])
        lf = LineFeeder(self._filename, self._algorithm)
        self.assertEquals([5, 44, 87], lf.search())

    def test_match_letter(self):
        self._algorithm.get_pattern = Mock(return_value = "a")
        self._algorithm.search = Mock(side_effect = [[0], [], [], [10], [], [], [4], [], []])
        lf = LineFeeder(self._filename, self._algorithm)
        self.assertEquals([5, 44, 87], lf.search())


if __name__ == '__main__':
    unittest.main()
