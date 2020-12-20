"""
Tests for the various operator pools.
"""
import unittest as ut

from diceroller.pools.operator import SumPool, SubtractPool, ProductPool, DivisionPool
from diceroller.pools.dice import DiceTypePool as Dice

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
