"""
Tests for the various operator pools.
"""
import unittest as ut

from diceroller.pools.operator import SumPool, SubtractPool, ProductPool, DivisionPool
from diceroller.pools.dice import dice

class BinaryOperatorTests(ut.TestCase):
    "Test cases for the binary operator."
    def assertProbSum(self, pool, msg="The probability for all values needs to add up to one"):
        "Assert whether the probabilites for the values sum to one"
        self.assertEqual(1, sum(pool.prob(val) for val in pool.values), msg=msg)

    def test_prob_sum_sum(self):
        "Test the sum for probabilities for the SumPool"
        pool = SumPool(dice(6, 2), dice(4, 3))
        self.assertProbSum(pool)

    def test_prob_sum_sub(self):
        "Test the sum for probabilities for the SubtractPool"
        pool = SubtractPool(dice(6, 2), dice(4, 3))
        self.assertProbSum(pool)

    def test_prob_sum_mul(self):
        "Test the sum for probabilities for the ProductPool"
        pool = ProductPool(dice(6, 2), dice(4, 3))
        self.assertProbSum(pool)

    def test_prob_sum_div(self):
        "Test the sum for probabilities for the DivisionPool"
        pool = DivisionPool(dice(6, 2), dice(4, 3))
        self.assertProbSum(pool)