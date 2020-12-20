"""
Tests for the various operator pools.
"""
import unittest as ut

from dicealyzer.pools.operator import SumPool, SubtractPool, ProductPool, DivisionPool, ConstPool
from dicealyzer.pools.dice import DiceTypePool as Dice

class BinaryOperatorTests(ut.TestCase):
    "Test cases for the binary operator."
    def assertProbSum(self, pool, msg="The probability for all values needs to add up to one"):
        "Assert whether the probabilites for the values sum to one"
        self.assertEqual(1, sum(pool.prob(val) for val in pool.values), msg=msg)

    def test_prob_sum_sum(self):
        "Test the sum for probabilities for the SumPool"
        pool = SumPool(Dice(6, 2), Dice(4, 3))
        self.assertProbSum(pool)

    def test_prob_sum_sub(self):
        "Test the sum for probabilities for the SubtractPool"
        pool = SubtractPool(Dice(6, 2), Dice(4, 3))
        self.assertProbSum(pool)

    def test_prob_sum_mul(self):
        "Test the sum for probabilities for the ProductPool"
        pool = ProductPool(Dice(6, 2), Dice(4, 3))
        self.assertProbSum(pool)

    def test_prob_sum_div(self):
        "Test the sum for probabilities for the DivisionPool"
        pool = DivisionPool(Dice(6, 2), Dice(4, 3))
        self.assertProbSum(pool)

class ConstCase(ut.TestCase):
    "Test case for the number pool"
    def test_roll(self):
        "Test if the roll always gives back the same value"
        pool = ConstPool(6)
        self.assertEqual(6, pool.roll()[0])

    def test_values(self):
        "Test is the values given back are only the number given"
        pool = ConstPool(5)
        self.assertEqual(1, len(pool.values))
        self.assertIn(5, pool.values)

    def test_probability(self):
        "Make sure the probability is always either one or zero"
        pool = ConstPool(4)
        self.assertEqual(0, pool.probability(3))
        self.assertEqual(1, pool.probability(4))
