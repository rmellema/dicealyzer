"""
Tests for the base Dice Pools, and interaction between them
"""
import unittest as ut

from diceroller.pools import NumberPool

class NumberCase(ut.TestCase):
    "Test case for the number pool"
    def test_roll(self):
        "Test if the roll always gives back the same value"
        pool = NumberPool(6)
        self.assertEqual(6, pool.roll()[0])

    def test_values(self):
        "Test is the values given back are only the number given"
        pool = NumberPool(5)
        self.assertEqual(1, len(pool.values))
        self.assertIn(5, pool.values)

    def test_probability(self):
        "Make sure the probability is always either one or zero"
        pool = NumberPool(4)
        self.assertEqual(0, pool.probability(3))
        self.assertEqual(1, pool.probability(4))
