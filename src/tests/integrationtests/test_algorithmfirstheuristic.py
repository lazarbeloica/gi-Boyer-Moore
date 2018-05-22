from src.tests.integrationtests.test_algorithm import TestAlgorithm
from src.heuristics.firstheuristic import FirstHeuristic

class TestAlgorithmFirstH(TestAlgorithm):
    
    def setUp(self):
        self.set_heuristic(FirstHeuristic())