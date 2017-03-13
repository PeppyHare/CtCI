import unittest

from algorithms import (coincounter, matrixflipper)


class TestChangeMaker(unittest.TestCase):
    def test_change_maker_1(self):
        ncoins = 3
        coins_list = [1, 2, 4]
        cash = 4
        expected_result = 4
        actual_result = coincounter.count(cash, ncoins, coins_list)
        self.assertEqual(expected_result, actual_result)

    def test_cahnge_maker_2(self):
        ncoins = 2
        coins_list = [1, 13]
        cash = 14
        expected_result = 2
        actual_result = coincounter.count(cash, ncoins, coins_list)
        self.assertEqual(expected_result, actual_result)


class TestMatrixFlipper(unittest.TestCase):
    def test_matrix_flipper_1(self):
        test_matrix = [[112, 42, 83, 119], [56, 125, 56, 49],
                       [15, 78, 101, 43], [62, 98, 114, 108]]
        expected = 414
        actual = matrixflipper.matrixflipper(2, test_matrix)
        self.assertEqual(expected, actual)
