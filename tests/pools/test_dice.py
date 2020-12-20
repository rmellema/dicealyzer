"""
Unittests for the pools.dice package.
"""
import unittest as ut

from diceroller.pools.dice import DiceTypePool, DiceDropPool

class DiceTypePoolTester(ut.TestCase):
    "Test case for the DiceTypePool"
    def test_values_one_die(self):
        "Tests if the values for one die are given correctly"
        pool = DiceTypePool(6)
        self.assertNotIn(0, pool.values, msg="0 is given as a valid values for a die")
        for x in range(1, 7):
            self.assertIn(x, pool.values, msg="Value in range not listed for die")
        self.assertNotIn(7, pool.values)

    def test_values_two_dice(self):
        "Tests if the possible values for two dice are given correctly"
        pool = DiceTypePool(4, 2)
        self.assertNotIn(0, pool.values, msg = "0 is given as a valid value for a die")
        self.assertNotIn(1, pool.values, msg="1 is given as a valid value for two dice")
        for x in range(2, 8):
            self.assertIn(x, pool.values, msg="Value in range not listed for die")
        self.assertNotIn(9, pool.values, msg="Value not in range given as a valid value")

    def test_enough_rolls(self):
        "Tests if enough dice gets rolled"
        pool = DiceTypePool(6, 4)
        self.assertEqual(4, len(pool.roll_all()),
                         msg="Wrong number of dice rolled")

    def test_probability_sum(self):
        "Tests if the sum of all probabilities is one"
        pool = DiceTypePool(6, 4)
        self.assertEqual(1, sum(pool.prob(v) for v in pool.values),
                         msg="Sum of probabilities does not add up to one")

    def test_probability(self):
        "Tests if the probabilities for 2d6 are calculated correctly"
        pool = DiceTypePool(6, 2)
        self.assertAlmostEqual(1/36, pool.prob(2),
                               msg="Probability for 2 calcualted incorrectly")
        self.assertAlmostEqual(2/36, pool.prob(3),
                               msg="Probability for 3 calcualted incorrectly")
        self.assertAlmostEqual(3/36, pool.prob(4),
                               msg="Probability for 4 calcualted incorrectly")
        self.assertAlmostEqual(4/36, pool.prob(5),
                               msg="Probability for 5 calcualted incorrectly")
        self.assertAlmostEqual(5/36, pool.prob(6),
                               msg="Probability for 6 calcualted incorrectly")
        self.assertAlmostEqual(6/36, pool.prob(7),
                               msg="Probability for 7 calcualted incorrectly")
        self.assertAlmostEqual(5/36, pool.prob(8),
                               msg="Probability for 8 calcualted incorrectly")
        self.assertAlmostEqual(4/36, pool.prob(9),
                               msg="Probability for 9 calcualted incorrectly")
        self.assertAlmostEqual(3/36, pool.prob(10),
                               msg="Probability for 10 calcualted incorrectly")
        self.assertAlmostEqual(2/36, pool.prob(11),
                               msg="Probability for 11 calcualted incorrectly")
        self.assertAlmostEqual(1/36, pool.prob(12),
                               msg="Probability for 12 calcualted incorrectly")

    def test_pred_prob(self):
        "Tests if the `pred_prob` for the equality predicate is the same as `probability`."
        pool = DiceTypePool(8, 4)
        for value in pool.values:
            self.assertEqual(pool.probability(value), pool.pred_prob(lambda x: x == value),
                             msg="The probability for a given value should be the same as the " +\
                             "probability that a roll is equal to that value.")

class TestDropPool(ut.TestCase):
    "Test case for the DiceDropPool"
    def test_normalization(self):
        "Test if the probabilities for the pool sum to one"
        pool = DiceDropPool(6, 5, 2)
        self.assertEqual(1, sum(pool.prob(v) for v in pool.values),
                         msg="Sum of probabilities does not add up to one")

    def test_lowest_probability(self):
        "Test to make sure that the dropping of dice leads to higher values"
        pool1 = DiceDropPool(6, 3, 1, False)
        pool2 = DiceTypePool(6, 2)
        self.assertEqual(pool1.values, pool2.values,
                         msg="Dropping a die should not change possible values")
        self.assertGreater(pool1.expected_value(), pool2.expected_value(),
                           msg="The probability for the dropping pool should be higher")
