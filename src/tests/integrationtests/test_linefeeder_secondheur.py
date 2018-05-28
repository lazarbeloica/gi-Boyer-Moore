from src.tests.integrationtests import test_linefeeder
from src.heuristics.secondheuristic import SecndHeuristic

class TestLineFeederBadCharacter(test_linefeeder.TestLineFeeder):

    def setUp(self):
        self.set_heuristic(SecndHeuristic())