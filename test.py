# M05 Programming Assignments
# Author: Joey Roberts
# Date: 2/16/2023
# Testing code tutorial

from fractions import Fraction
import unittest

# imports sum function from my_sum folder
from my_sum import sum

#Creates a class called TestSum
class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        # Takes data from list and sums data
        data = [1, 2, 3]
        result = sum(data)
        # Test the result to see if it is equal to 6
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()