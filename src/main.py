from src.heuristics.compositeheuristic import CompositeHeuristic
from src.heuristics.badcharacter import BadCharacter
from src.heuristics.firstheuristic import FirstHeuristic
from src.heuristics.secondheuristic import SecndHeuristic
from src.heuristics.goodsuffix import GoodSuffix
from src.performance.performanceanalyser import PerformanceAnalyser
import sys
import os.path
from src.algorithm.boyermoore import BoyerMoore

heur_dict = {'BC': BadCharacter,
             'bc': BadCharacter,
             'FH': FirstHeuristic,
             'fh': FirstHeuristic,
             'GS': GoodSuffix,
             'gs': GoodSuffix,
             'SH': SecndHeuristic,
             'sh': SecndHeuristic
             }
    
def read_arguments(arg_list):
    algo_list = []
    comb_list = []
    reading_heur = False
    reading_comb = False
    reading_path_pattern = True
    path = ''
    pattern = ''
    for arg in arg_list:
        if '-h' in arg:
            reading_heur = True
            reading_comb = False
        elif '-c' in arg:
            reading_heur = False
            reading_comb = True
        elif reading_comb:
            if reading_path_pattern:
                path = arg
                if not os.path.isfile(path):
                    raise Exception("File (" + path + ") doesn't exist")
            else:
                pattern = arg
                comb_list.append((path, pattern))
            reading_path_pattern = not reading_path_pattern
        elif reading_heur:
            if '+' in arg:
                if any(composite_part not in heur_dict for composite_part in arg.split('+')):
                    raise Exception('Wrong input for heuristic')
                c_h_list = [heur_dict[composite_part]() for composite_part in arg.split('+')]
                algo_list.append(BoyerMoore(CompositeHeuristic(c_h_list)))
            else:
                if arg not in heur_dict:
                    raise Exception('Wrong input for heuristic')
                algo_list.append(BoyerMoore(heur_dict[arg]()))
                
    return algo_list, comb_list


if __name__ == '__main__':

    pa = PerformanceAnalyser()
    algo_list, comb_list = read_arguments(sys.argv)
    
    for algo in algo_list:
        pa.add_algorithm(algo)
        
    for path, pattern in comb_list:
        pa.add_path_pattern(path, pattern)
        
    pa.analyse()
    pa.show_results()
                    
