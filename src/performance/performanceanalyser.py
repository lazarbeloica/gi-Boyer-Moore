from src.representations.barcharttable import BarChartTable
from memory_profiler import memory_usage
import time
import statistics
from src.utils.linefeeder import LineFeeder

def timer_decorator(f):
    def wrapper(*arg, **kwarg):
        start_time = time.time()
        f(*arg, **kwarg)
        end_time = time.time()

        return end_time - start_time

    return wrapper

<<<<<<< 24fb4775f9c555e4e4eee10d201d0bb12765f5ce
def memory_decorator(f):
    def wrapper(execution_time):
        interval = int(execution_time/40) if int(execution_time/40) != 0 else 1
        mem_usage_list = memory_usage(f, interval=interval)
        return statistics.mean(mem_usage_list)

    return wrapper


=======
>>>>>>> unstable
class PerformanceAnalyser:

    def __init__(self):
        self._line_feeder = LineFeeder()
        self._combinations = [] # combination of file path and pattern
        self._algorithms = set()
        self._time_results = {}
        self._mem_results = {}
        self._tick_labels = []

    def add_path_pattern(self, path, pattern):
        self._combinations.append((path, pattern))

    def add_algorithm(self, algorithm_):
        self._algorithms.add(algorithm_)


    def analyse(self):

        for path, pattern in self._combinations:
            self._tick_labels.append('PATTERN: ' + pattern + '     PATH: ' + path)
            for algo in self._algorithms:

                algo.set_pattern(pattern)
                self._line_feeder.set_algorithm(algo)
                self._line_feeder.set_file_path(path)

                execution_time = timer_decorator(self._line_feeder.get_results)()
                self._time_results.setdefault(algo.get_name(), []).append(execution_time)

                algo.set_pattern(pattern)
                self._line_feeder.set_algorithm(algo)
                self._line_feeder.set_file_path(path)

                self._mem_results.setdefault(algo.get_name(), []).append(memory_decorator(self._line_feeder.get_results)(execution_time))

    def show_results(self):
        BarChartTable.create_result_window("Time analysis", '', 'Time(sec)', self._time_results, [str(i + 1) for i in range(len(self._tick_labels))])
        BarChartTable.create_result_window("Memory analysis", '', 'Memory(MB)', self._mem_results, [str(i + 1) for i in range(len(self._tick_labels))])
        data = [[str(i + 1), elem] for i, elem in enumerate(self._tick_labels)]
        BarChartTable.create_table(data)
        BarChartTable.show_result()
