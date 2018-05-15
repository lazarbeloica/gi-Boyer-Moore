from src.tests.integrationtests import test_algorithm
from src.heuristics.goodsuffix import GoodSuffix

class TestAlgorithmGoodSuffix(test_algorithm.TestAlgorithm):
    
    def setUp(self):
        self.set_heuristic(GoodSuffix())