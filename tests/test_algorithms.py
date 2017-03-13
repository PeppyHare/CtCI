import unittest

from algorithms import (coincounter, matrixflipper, bonappetit)


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


class TestBonAppetit(unittest.TestCase):
    def test_bonappetit_1(self):
        k = 1
        costs = [3, 10, 2, 9]
        bill = 12
        expected = 5
        actual = bonappetit.bonappetit(k, costs, bill)
        self.assertEqual(expected, actual)

    def test_bonappetit_2(self):
        k = 1
        costs = [3, 10, 2, 9]
        bill = 7
        expected = "Bon Appetit"
        actual = bonappetit.bonappetit(k, costs, bill)
        self.assertEqual(expected, actual)
