from src.tests.integrationtests import test_algorithm
from src.heuristics.badcharacter import BadCharacter

class TestAlgorithmBadCharacter(test_algorithm.TestAlgorithm):
    
    def setUp(self):
        self.set_heuristic(BadCharacter())