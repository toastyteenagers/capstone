import sys
import unittest
from PyQt6 import QtWidgets
from main import MainApplication

app = QtWidgets.QApplication(sys.argv)

class TestMainApplication(unittest.TestCase):
    def setUp(self):
        self.mainApp = MainApplication()

    def test_widget_count(self):
        expected_count = 3
        actual_count = self.mainApp.stackedWidget.count()
        self.assertEqual(actual_count, expected_count)

    def test_initial_screen_displayed(self):
        current_widget = self.mainApp.stackedWidget.currentWidget()
        self.assertIs(current_widget, self.mainApp.startupScreen)

if __name__ == '__main__':
    unittest.main()
