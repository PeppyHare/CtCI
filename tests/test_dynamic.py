import unittest

from dynamicprogramming import coincounter


class TestChangeMaker(unittest.TestCase):
    def test_change_maker(self):
        ncoins = 3
        coins_list = [1, 2, 4]
        cash = 4
        expected_result = 4
        actual_result = coincounter.count(cash, ncoins, coins_list)
        self.assertEqual(expected_result, actual_result)
