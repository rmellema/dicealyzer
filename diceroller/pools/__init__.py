"""
A module to represent dice pools before they are rolled.

A dice pool is a collection of dice or numbers that can be combined in various ways, and rolled
later on. The package also offers a few ways to analyse the values that it can roll and how likely
that is.

Dice pools are assumed to produce numbers, but that is only necessary if they are combined with the
standard dice pools defined in this package. Otherwise, you can use any custom type, as long as it
is discrete.
"""
from .base import AbstractDicePool
from .dice import DiceTypePool, DiceDropPool
from .operator import *

class NumberPool(AbstractDicePool):
    """
    A class to represent single numbers without rolling. Useful for combing with other dice pools.
    """
    def __init__(self, n):
        self.number = n

    def __str__(self):
        return str(self.number)

    def roll(self):
        # There are no dice rolled here, so return an empty list
        return self.number, []

    @property
    def values(self):
        return set([self.number])

    def probability(self, value):
        if value != self.number:
            return 0
        return 1
