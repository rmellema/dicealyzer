"""
The base module for all dice pools.
"""
from abc import ABC, abstractmethod

class AbstractDicePool(ABC):
    """
    The abstract base class for all dice pools.
    """
    @abstractmethod
    def roll(self):
        """
        Roll the dice in this pool, and return the result. Also returns the values of all rolled
        dice.
        """

    def pretty_string(self):
        "Print the dice pool in a pretty manner"
        return str(self)

    @abstractmethod
    def __str__(self):
        pass

    @property
    @abstractmethod
    def values(self):
        "All the possible values that this dice pool can produce."

    @abstractmethod
    def probability(self, value):
        "Returns the probability of a certain value being rolled."

    def prob(self, value):
        "Alias for `probability`"
        return self.probability(value)

    def cond_prob(self, pred):
        "Calculate the probability that a roll from this dice pool adheres to the given predicate"
        return sum(self.prob(val) for val in self.values if pred(val))

    def expected_value(self):
        "Returns the expected value of this dice pool."
        return sum(self.probability(value) * value for value in self.values)
