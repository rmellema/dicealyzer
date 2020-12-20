"""
The module for dice pools consisting of other different dice pools. It also installs operators on
`AbstractDicePool` to make it easier to combine dice pools in Python.
"""
from functools import reduce
from itertools import chain, product
from operator import add, sub, mul, truediv as div

from .base import AbstractDicePool

class BinaryOperatorPool(AbstractDicePool):
    """
    A class to represent multiple dice pools that are combined by an operator. This operator is
    assumed to work with the python function `reduce`.
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

    def __repr__(self):
        str_operands = ', '.join([repr(operand) for operand in self.operands])
        return '{}.BinaryOperatorPool({}, {}, {})'.format(__name__,
                                                          repr(self.operator),
                                                          repr(self.operator_str),
                                                          str_operands)

class SumPool(BinaryOperatorPool):
    "Create a sum of multiple dice pools."
    def __init__(self, *operands):
        super().__init__(add, '+', *operands)

class SubtractPool(BinaryOperatorPool):
    "Create a negative sum of multiple dice pools."
    def __init__(self, *operands):
        super().__init__(sub, '-', *operands)

class ProductPool(BinaryOperatorPool):
    "Create a product of multiple dice pools."
    def __init__(self, *operands):
        super().__init__(mul, '*', *operands)

class DivisionPool(BinaryOperatorPool):
    "Create a fraction of multiple dice pools."
    def __init__(self, *operands):
        super().__init__(div, '/', *operands)

class ConstPool(AbstractDicePool):
    """
    A class to represent a single constant value without rolling. Useful for combing with other dice
    pools.
    """
    def __init__(self, n):
        self.const = n

    def __str__(self):
        return str(self.const)

    def __repr__(self):
        return '{}.ConstPool({})'.format(__name__, self.const)

    def roll(self):
        # There are no dice rolled here, so return an empty list
        return self.const, []

    @property
    def values(self):
        return set([self.const])

    def probability(self, value):
        if value != self.const:
            return 0
        return 1

def def_op_func(cls):
    "Defines a python function that can be used on a class for operator overloading."
    def op_func(lhs, rhs):
        if not isinstance(rhs, AbstractDicePool):
            rhs = ConstPool(rhs)
        return cls(lhs, rhs).simplify()
    return op_func

AbstractDicePool.__add__ = def_op_func(SumPool)
AbstractDicePool.__sub__ = def_op_func(SubtractPool)
AbstractDicePool.__mul__ = def_op_func(ProductPool)
AbstractDicePool.__truediv__ = def_op_func(DivisionPool)
