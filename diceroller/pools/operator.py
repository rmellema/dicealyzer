"""
The module for dice pools consisting of other different dice pools.
"""
from functools import reduce
from itertools import chain, product
from operator import add, sub, mul, truediv as div

from .base import AbstractDicePool

class BinaryOperatorPool(AbstractDicePool):
    """
    A class to represent a dicepool with multiple types of dice.
    """
    def __init__(self, operator, operator_str, *operands):
        self.operator = operator
        self.operator_str = operator_str
        self.operands = operands
        self._prob = {}

    def pretty_string(self):
        return '(' + str(self) + ')'

    def roll(self):
        rolls = [operand.roll() if isinstance(operand, AbstractDicePool) else (operand, [])
                                for operand in self.operands]
        sums = map(lambda r: r[0], rolls)
        dice = map(lambda r: r[1], rolls)
        return reduce(self.operator, sums), list(chain.from_iterable(dice))

    def simplify(self):
        "Simplify this Pool so it does not contain instances of the same type."
        self.operands = list(chain.from_iterable(operand.operands
                if isinstance(operand, BinaryOperatorPool) and self.operator == operand.operator
                else [operand]
                for operand in self.operands))
        return self

    @property
    def values(self):
        combinations = product(*[op.values for op in self.operands])
        return set(map(lambda c: reduce(self.operator, c), combinations))

    def probability(self, value):
        if value in self._prob:
            return self._prob[value]
        if value not in self.values:
            return 0
        combinations = product(*[op.values for op in self.operands])
        valid_combs = filter(lambda c: reduce(self.operator, c) == value, combinations)
        return sum(reduce(mul, map(lambda p, v: p.probability(v), self.operands, comb))
                   for comb in valid_combs)

    def __str__(self):
        str_operands = [operand.pretty_string()
                        if isinstance(operand, AbstractDicePool) else str(operand)
                        for operand in self.operands]
        return ' {} '.format(self.operator_str).join(str_operands)

class SumPool(BinaryOperatorPool):
    "Create a sum of multiple dice pools."
    def __init__(self, *operands):
        super().__init__(add, '+', *operands)
AbstractDicePool.__add__ = lambda l, r: SumPool(l, r).simplify()

class SubtractPool(BinaryOperatorPool):
    "Create a negative sum of multiple dice pools."
    def __init__(self, *operands):
        super().__init__(sub, '-', *operands)
AbstractDicePool.__sub__ = lambda l, r: SubtractPool(l, r).simplify()

class ProductPool(BinaryOperatorPool):
    "Create a product of multiple dice pools."
    def __init__(self, *operands):
        super().__init__(mul, '*', *operands)
AbstractDicePool.__mul__ = lambda l, r: ProductPool(l, r).simplify()

class DivisionPool(BinaryOperatorPool):
    "Create a fraction of multiple dice pools."
    def __init__(self, *operands):
        super().__init__(div, '/', *operands)
AbstractDicePool.__truediv__ = lambda l, r: DivisionPool(l, r).simplify()
