import unittest

from dynamicprogramming import coincounter


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
