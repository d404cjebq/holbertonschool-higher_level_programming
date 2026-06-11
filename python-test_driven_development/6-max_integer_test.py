#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_regular_list(self):
        """Test with a normal list of positive integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test with max integer at the beginning."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test with max integer in the middle."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_single_element(self):
        """Test with a single element list."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test with an empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """Test with no argument (default empty list) returns None."""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """Test with all negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_positive_negative(self):
        """Test with mixed positive and negative numbers."""
        self.assertEqual(max_integer([-10, 0, 5, -3]), 5)

    def test_identical_elements(self):
        """Test with all identical elements."""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_one_negative(self):
        """Test list with one negative and rest positive."""
        self.assertEqual(max_integer([-1, 1, 2, 3]), 3)

    def test_floats(self):
        """Test with float values."""
        self.assertEqual(max_integer([1.5, 2.7, 0.3, 2.6]), 2.7)

    def test_mixed_int_float(self):
        """Test with mixed integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 3, 0.5]), 3)

    def test_large_numbers(self):
        """Test with very large numbers."""
        self.assertEqual(max_integer([999999, 1000000, 999998]), 1000000)

    def test_two_elements(self):
        """Test with exactly two elements."""
        self.assertEqual(max_integer([3, 7]), 7)
        self.assertEqual(max_integer([7, 3]), 7)

    def test_zero_in_list(self):
        """Test with zero in the list."""
        self.assertEqual(max_integer([0, 0, 0]), 0)
        self.assertEqual(max_integer([-1, 0, 1]), 1)


if __name__ == '__main__':
    unittest.main()
