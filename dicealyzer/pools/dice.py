"""
A module to represent dice pools consisting of one type of dice.
"""
from fractions import Fraction
from itertools import product
from random import randint

from .base import AbstractDicePool

class DiceTypePool(AbstractDicePool):
    """
    A class to represent a dicepool with multiple of one dice.
    """
    def __init__(self, sides, amount=1):
        self.amount = amount
        self.sides = sides
        self._prob = {}

    def roll_all(self):
        "Roll all the dice in this pool and return results as a list"
        return [randint(1, self.sides) for _ in range(self.amount)]

    def roll(self):
        rolls = self.roll_all()
        return sum(rolls), rolls

    def __str__(self):
        return '{}d{}'.format(self.amount, self.sides)

    def __repr__(self):
        return '{}.DiceTypePool(sides={}, amount={})'.format(__name__, self.sides, self.amount)

    @property
    def values(self):
        return set(range(self.amount, self.sides * self.amount + 1))

    def probability(self, value):
        if value in self._prob:
            return self._prob[value]
        if value not in self.values:
            return 0
        possibilities = self.sides ** self.amount
        rolls = product(range(1, self.sides + 1), repeat=self.amount)
        values = map(sum, rolls)
        prob = Fraction(len([x for x in values if x == value]),possibilities)
        self._prob[value] = prob
        return prob

class DiceDropPool(DiceTypePool):
    """
    A class to represent a dicepool where the lowest or highest dice are dropped.
    """
    def __init__(self, sides, amount=2, drop=1, highest=False):
        super().__init__(sides, amount)
        self.drop = drop
        self.highest = highest

    def _drop_rolls(self, rolls):
        return sorted(rolls)[self.drop:]

    def roll(self):
        rolls = self.roll_all()
        return sum(self._drop_rolls(rolls)), rolls

    @property
    def values(self):
        left = self.amount - self.drop
        return set(range(left, self.sides * left + 1))

    def probability(self, value):
        if value in self._prob:
            return self._prob[value]
        if value not in self.values:
            return 0
        possibilities = self.sides ** self.amount
        rolls = product(range(1, self.sides + 1), repeat=self.amount)
        values = map(lambda r: sum(self._drop_rolls(r)), rolls)
        prob = Fraction(len([x for x in values if x == value]), possibilities)
        self._prob[value] = prob
        return prob

    def __str__(self):
        if self.drop == 1:
            return super().__str__() + '-' + ('H' if self.highest else 'L')
        return super().__str__() + ('l' if self.highest else 'h') + str(self.drop)

    def __repr__(self):
        return '{}.DiceDropPool(sides={}, amount={}, drop={}, highest={})'\
                    .format(__name__, self.sides, self.amount, self.drop, self.highest)
