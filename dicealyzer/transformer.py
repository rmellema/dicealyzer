"""
This module contains the transformer class, that turns a given parse tree into a dice pool.
"""
from operator import add, sub, mul, truediv

from lark.visitors import Transformer, v_args

from .pools import BinaryOperatorPool, DiceTypePool, DiceDropPool, ConstPool

def keep_sum(rolls, keep, lowest=False):
    "A small helper function for keeping certain dice rolls"
    rolls.sort(reverse=lowest)
    return sum(rolls[len(rolls) - keep:])

@v_args(inline=True)
class DicePoolTransformer(Transformer):
    "Transforms a read statement into a dice pool that can be rolled multiple times."
    # pylint: disable=no-self-use, invalid-name
    def number(self, n):
        "Numbers should be read as ints."
        return int(n)

    def constpool(self, n):
        "The constpool rule only read NumberPools, so return one of those."
        return ConstPool(n)

    def dice(self, *values):
        "This rule reads in the number of dice and their sides. Returns them as a tuple of ints."
        try:
            amount, sides = values
        except ValueError:
            amount = 1
            sides = values[0]
        return (amount, sides)

    def pool(self, dice):
        "Reads in a simple dice pool."
        return DiceTypePool(dice[1], dice[0])

    def drop_lowest(self, dice):
        "Reads in a dice pool that drops the lowest dice."
        return DiceDropPool(dice[1], dice[0], 1, False)

    def drop_highest(self, dice):
        "Reads in a dice pool that drops the highest dice."
        return DiceDropPool(dice[1], dice[0], 1, True)

    def keep_highest(self, dice, keep):
        "Reads in a dice pool that keeps the `keep` highest."
        return DiceDropPool(dice[1], dice[0], keep, False)

    def keep_lowest(self, dice, keep):
        "Reads in a dice pool that drops the `keep` lowest."
        return DiceDropPool(dice[1], dice[0], keep, True)

    def add(self, p1, p2):
        "Combined several dice pools by adding them up."
        return BinaryOperatorPool(add, '+', p1, p2).simplify()

    def sub(self, p1, p2):
        "Combined several dice pools by subtracting them."
        return BinaryOperatorPool(sub, '-', p1, p2).simplify()

    def mul(self, p1, p2):
        "Combined several dice pools by multipolying them."
        return BinaryOperatorPool(mul, '*', p1, p2).simplify()

    def div(self, p1, p2):
        "Combined several dice pools by dividing them."
        return BinaryOperatorPool(truediv, '/', p1, p2).simplify()

    def start(self, *n):
        "This grammar only returns one object, which is a dice pool."
        try:
            return n[0]
        except IndexError:
            return None
