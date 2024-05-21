#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_empty(self):
        """Test if list is empty"""
        self.assertEqual(max_integer([]), None)

    def test_only_one(self):
        """Test if list contain only one element"""
        self.assertEqual(max_integer([1]), 1)

    def test_max_begin(self):
        """Test if list contain max value at the beginning"""
        self.assertEqual(max_integer([4, 3, 2]), 4)

    def test_max_mid(self):
        """Test if list contain max value at the middle"""
        self.assertEqual(max_integer([3, 4, 2]), 4)

    def test_max_end(self):
        """Test if list contain max value at the end"""
        self.assertEqual(max_integer([2, 3, 4]), 4)

    def test_max_one_is_negative(self):
        """Test if list contain one negative element"""
        self.assertEqual(max_integer([2, -3, 4]), 4)

    def test_max_all_are_negative(self):
        """Test if list contain only negative element"""
        self.assertEqual(max_integer([-2, -3, -4]), -2)


if __name__ == '__main__':
    unittest.main()
