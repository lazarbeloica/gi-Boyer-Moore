from src.tests.integrationtests import test_linefeeder
from src.heuristics.goodsuffix import GoodSuffix

class TestLineFeederGoodSuffix(test_linefeeder.TestLineFeeder):

    def setUp(self):
        self.set_heuristic(GoodSuffix())