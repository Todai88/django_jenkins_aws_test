import os
from unittest import TestCase

from Scripts.calculator import Calculator

class TestCalculator(TestCase):
    def setUp(self):
        self.THIS_DIR = os.path.dirname(os.path.abspath(__file__))

    def test_valid_add(self):
        expected = 2
        actual = Calculator().add(1, 1)

        self.assertEqual(expected, actual, "Incorrect addition result\n")
