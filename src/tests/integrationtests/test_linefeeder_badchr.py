from src.tests.integrationtests import test_linefeeder
from src.heuristics.badcharacter import BadCharacter

class TestLineFeederBadCharacter(test_linefeeder.TestLineFeeder):

    def setUp(self):
        self.set_heuristic(BadCharacter())