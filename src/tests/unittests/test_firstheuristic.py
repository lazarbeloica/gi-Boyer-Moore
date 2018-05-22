import unittest
from src.heuristics.firstheuristic import FirstHeuristic

class TestFirstHeuristic(unittest.TestCase):
    
    def setUp(self):
        self.heuristics = FirstHeuristic()


    def test_shift_found_0(self):
        '''
        cbbacacaabaaaaaa
        cbba
        ****cbba  <- resulting
        '''
        self.pattern = "cbba"
        self.heuristics.preprocess(self.pattern)
        text = "cbbacacaabaaaaaa"
        res = self.heuristics.get_shift_pattern_found(next_letter=text[3 + 1])
        self.assertEqual(res,4)

    def test_shift_found_1(self):
        '''
        cbbabacaabaaaaaa
        cbba
        **cbba    <- resulting
        '''
        self.pattern = "cbba"
        self.heuristics.preprocess(self.pattern)
        text = "cbbabacaabaaaaaa"
        res = self.heuristics.get_shift_pattern_found(next_letter=text[3 + 1])
        self.assertEqual(res,2)

    def test_shift_found_2(self):
        '''
        cbbaxacaabaaaaaa
        cbba
        **** cbba   <- resulting
        '''
        self.pattern = "cbba"
        self.heuristics.preprocess(self.pattern)
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
        self.pattern = "cbba"
        self.heuristics.preprocess(self.pattern)
        text = "cbbaxacaabaacbbac"
        res = self.heuristics.get_shift_pattern_found(next_letter=text[16])
        self.assertEqual(res,4)
        
    def test_shift_not_found_0(self):
        
        '''
        stringmatching
        pattern
            >>>pattern
        '''
        self.pattern = "pattern"
        self.heuristics.preprocess(self.pattern)
        res = self.heuristics.get_shift_pattern_not_found(aligned_letter = 'g')
        self.assertEqual(res,7)

                    
    def test_shift_not_found_1(self):
        '''istofindthepattern
           pattern
               >>>pattern
        '''
        self.pattern = "pattern"
        self.heuristics.preprocess(self.pattern)
        res = self.heuristics.get_shift_pattern_not_found(aligned_letter = 'n')
        self.assertEqual(res,7)
        
    def test_shift_not_found_2(self):
        '''dthepattern
           pattern
            >>pattern
        ''' 
        self.pattern = "pattern"
        self.heuristics.preprocess(self.pattern) 
        res = self.heuristics.get_shift_pattern_not_found(aligned_letter = 't')
        self.assertEqual(res,3)
        
if __name__ == '__main__':
    unittest.main()