"""
The base module for all dice pools.
"""
from abc import ABC, abstractmethod

class AbstractDicePool(ABC):
    """
    The abstract base class for all dice pools. Defines several convinience methods based on the
    abstract methods presented.
    """
    @abstractmethod
    def roll(self):
        """
        Roll the dice in this pool, and return the result. Also returns the values of all rolled
        dice as a list.
        """

    def pretty_string(self):
        "Print the dice pool in a pretty manner."
        return str(self)

    @abstractmethod
    def __str__(self):
        pass

    @property
    @abstractmethod
    def values(self):
        """
        All the possible values that this dice pool can produce, as a set. Ascending order is
        preferred, but not required.
        """

    @abstractmethod
    def probability(self, value):
        "Returns the probability of a certain value being rolled."

    def prob(self, value):
        "Alias for `probability`"
        return self.probability(value)

    def pred_prob(self, pred):
        "Calculate the probability that a roll from this dice pool adheres to the given predicate"
        return sum(self.prob(val) for val in self.values if pred(val))

    def prob_greater_than(self, value):
        "Give the probability that this dice pool rolls a number higher than `value`."
        return self.pred_prob(lambda x: x > value)

    def prob_greater_equal(self, value):
        "Give the probability that this dice pool rolls equal to or higher than `value`."
        return self.pred_prob(lambda x: x >= value)

    def prob_less_than(self, value):
        "Give the probability that this dice pool rolls a number strictly lower than `value`."
        return self.pred_prob(lambda x: x < value)

    def prob_less_equal(self, value):
        "Give the probability that this dice pool rolls equal to or lower than `value`."
        return self.pred_prob(lambda x: x <= value)

    def expected_value(self):
        "Returns the expected value of this dice pool."
        return sum(self.probability(value) * value for value in self.values)
