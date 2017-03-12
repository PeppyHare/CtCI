import unittest

from sorting import quicksort


class TestSorting(unittest.TestCase):
    def test_quicksort(self):
        test_input = [2, 1]
        expected = [1, 2]
        actual = quicksort.quicksort(test_input)
        self.assertEqual(expected, actual)
