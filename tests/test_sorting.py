import unittest
import random

from sorting import quicksort, heapsort, mergesort, bubblesort, insertionsort


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


class TestMergesort(unittest.TestCase):
    def setUp(self):
        self.random_data = [random.random() for i in range(0, 1000)]
        self.sorted_data = sorted(self.random_data)

    def test_1(self):
        actual = mergesort.mergesort(self.random_data)
        self.assertListEqual(self.sorted_data, actual)


class TestBubblesort(unittest.TestCase):
    def setUp(self):
        # Smaller case, poor bubble sort
        self.random_data = [random.random() for i in range(0, 100)]
        self.sorted_data = sorted(self.random_data)

    def test_1(self):
        actual = bubblesort.bubblesort(self.random_data)
        self.assertListEqual(self.sorted_data, actual)


class TestInsertionSort(unittest.TestCase):
    def setUp(self):
        self.random_data = [random.random() for i in range(0, 100)]
        self.sorted_data = sorted(self.random_data)

    def test_1(self):
        actual = insertionsort.insertionsort(self.random_data)
        self.assertListEqual(self.sorted_data, actual)
