from heuristics.compositeheuristic import CompositeHeuristic
from heuristics.badcharacter import BadCharacter
from heuristics.goodsuffix import GoodSuffix
from performance.performanceanalyser import PerformanceAnalyser

if __name__ == '__main__':
    pa = PerformanceAnalyser("ATGATG", "/home/aviator/Desktop/cfa_ref_CanFam3.1_chr1.fa")
    pa.add_heuristic(BadCharacter())
    pa.add_heuristic(GoodSuffix())
    pa.add_heuristic(CompositeHeuristic(GoodSuffix(),BadCharacter()))
    pa.analyse()
    pa.show_results()
