import unittest
import random
import timeit
import pickle
import sys

from sorting import quicksort, heapsort


class TestQuicksort(unittest.TestCase):
    def setUp(self):
        self.random_data = [random.random() for i in range(0, 1000)]
        self.sorted_data = sorted(self.random_data)

    def test_1(self):
        actual = quicksort.quicksort(self.random_data)
        self.assertListEqual(self.sorted_data, actual)


class TestHeapsort(unittest.TestCase):
    def setUp(self):
        self.random_data = [random.random() for i in range(0, 1000)]
        self.sorted_data = sorted(self.random_data)

    def test_1(self):
        actual = heapsort.heapsort(self.random_data)
        self.assertListEqual(self.sorted_data, actual)
