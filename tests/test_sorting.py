import unittest
import random

from sorting import (quicksort, heapsort, mergesort, bubblesort, insertionsort,
                     selectionsort, radixsort, bucketsort)


class SortingAlgorithmTestCase(unittest.TestCase):
    """
    Shared setup/teardown for sorting algorithm test cases
    """

    def setUp(self):
        self.input = [random.random() for i in range(0, 100)]
        self.expected = sorted(self.input)


class TestQuicksort(SortingAlgorithmTestCase):
    def test_quicksort(self):
        actual = quicksort.quicksort(self.input)
        self.assertListEqual(self.expected, actual)


class TestHeapsort(SortingAlgorithmTestCase):
    def test_heapsort(self):
        actual = heapsort.heapsort(self.input)
        self.assertListEqual(self.expected, actual)


class TestMergesort(SortingAlgorithmTestCase):
    def test_mergesort(self):
        actual = mergesort.mergesort(self.input)
        self.assertListEqual(self.expected, actual)


class TestBubblesort(SortingAlgorithmTestCase):
    def test_bubblesort(self):
        actual = bubblesort.bubblesort(self.input)
        self.assertListEqual(self.expected, actual)


class TestInsertionSort(SortingAlgorithmTestCase):
    def test_insertionsort(self):
        actual = insertionsort.insertionsort(self.input)
        self.assertListEqual(self.expected, actual)


class TestSelectionSort(SortingAlgorithmTestCase):
    def test_selectionsort(self):
        actual = selectionsort.selectionsort(self.input)
        self.assertListEqual(self.expected, actual)


class TestRadixSort(unittest.TestCase):
    def setUp(self):
        self.input = list(range(100))
        random.shuffle(self.input)
        self.expected = sorted(self.input)

    def test_radixsort(self):
        actual = radixsort.radixsort(self.input)
        self.assertListEqual(self.expected, actual)


class TestBucketSort(SortingAlgorithmTestCase):
    def setUp(self):
        self.input = list(range(100))
        random.shuffle(self.input)
        self.expected = sorted(self.input)

    def test_bucketsort(self):
        actual = bucketsort.bucketsort(self.input)
        self.assertListEqual(self.expected, actual)
