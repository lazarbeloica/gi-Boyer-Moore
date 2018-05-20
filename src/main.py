from src.heuristics.badcharacter import BadCharacter
from src.heuristics.goodsuffix import GoodSuffix
from src.heuristics.compositeheuristic import CompositeHeuristic
from src.performance.performanceanalyser import PerformanceAnalyser

if __name__ == '__main__':
    pa = PerformanceAnalyser()
    pa.add_heuristic(BadCharacter())
    pa.add_heuristic(GoodSuffix())
    pa.add_heuristic(CompositeHeuristic(GoodSuffix(),BadCharacter()))
    pa.analyse("asdjasdvhajsdvajsdbhasjd asdbha sjasdjasvbdjas", "jasdj")
    pa.analyse("asdjasdvhajsdvajsdbhasjd asdbha sjasdjasvbdjas", "asff")
    pa.show_results()