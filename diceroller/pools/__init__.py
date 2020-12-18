"""
A module to represent dice pools before they are rolled.
"""
from .base import AbstractDicePool
from .dice import DiceTypePool, DiceDropPool
from .operator import *

class NumberPool(AbstractDicePool):
    """
    A class to represent single numbers without rolling.
    """
    def __init__(self, n):
        self.number = n

    def __str__(self):
        return str(self.number)

    def roll(self):
        return self.number, []

    @property
    def values(self):
        return set([self.number])

    def probability(self, value):
        if value != self.number:
            return 0
        return 1

def num(number):
    "Alias for creating a numberpool."
    return NumberPool(number)
