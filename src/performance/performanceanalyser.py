from algorithm.boyermoore import BoyerMoore
from representations.barcharttable import BarChartTable
from memory_profiler import memory_usage
import time
import statistics
from utils.linefeeder import LineFeeder

class PerformanceAnalyser:

    def __init__(self, pattern=None, filename=None, text=None):

        self._algorithm = BoyerMoore()
        self._heuristics = set()
        self._time_results = {}
        self._mem_results = {}
        self._tick_labels = []

        if filename is not None:
            self._lf = LineFeeder(filename, self._algorithm, pattern)
            self._matcher = self._lf
        else:
            self._matcher = self._algorithm

    def add_heuristic(self, heuristic_):
        self._heuristics.add(heuristic_)

    def remove_heuristic(self, heuristic_):
        self._heuristics.remove(heuristic_)

    def analyse(self):
        self._tick_labels.append("Pattern name \n Text name") #TODO
        for heuristic in self._heuristics:
            start_time = int(time.time())
            self._algorithm.set_heuristic(heuristic)

            self._matcher.search()
            end_time = int(time.time())
            operation_time = (end_time-start_time) #TODO time in seconds
            self._time_results.setdefault(heuristic.get_name(), []).append(operation_time)

            mem_usage_list = memory_usage(self._matcher.search, interval=20)
            self._mem_results.setdefault(heuristic.get_name(), []).append(statistics.mean(mem_usage_list))

    def show_results(self):
        BarChartTable.create_result_window("Time analysis", '', 'Time(sec)', self._time_results, self._tick_labels)
        BarChartTable.create_result_window("Memory analysis", '', 'Memory(MB)', self._mem_results, self._tick_labels)
        BarChartTable.show_result()
