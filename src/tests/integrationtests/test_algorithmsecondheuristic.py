from src.tests.integrationtests.test_algorithm import TestAlgorithm
from src.heuristics.secondheuristic import SecndHeuristic

class TestAlgorithmSecndH(TestAlgorithm):

    def setUp(self):
        self.set_heuristic(SecndHeuristic())