import unittest
from src.representations.barcharttable import BarChartTable

class TestBarChartTable(unittest.TestCase):
    
    def test_create_result_window_one(self):
        with self.assertRaisesRegex(Exception, "Each label has to have the same number of values"):
            BarChartTable.create_result_window("title", "x_label", "y_label", {'Label1':[3,2,5],'Label2':[2]}, ['tick1', 'tick2', 'tick3'])
            
    def test_create_result_window_two(self):
        with self.assertRaisesRegex(Exception, "Tick labels and every label must have the same number of items"):
            BarChartTable.create_result_window("title", "x_label", "y_label", {'Label1':[3,2],'Label2':[2,1]}, ['tick1', 'tick2', 'tick3'])
            