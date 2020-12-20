"""
This module provides ways to define and combine pools of dice so they can be analyzed.
"""
import pathlib
from functools import reduce
from lark import Lark

from . import pools, transformer
__VERSION__ = '0.0.1'

def get_parser():
    """
    Get the parser for parsing the dice notation. Returns a :py:class:`lark.Lark`
    """
    _grammar_file = pathlib.Path(__file__).parent.absolute() / 'grammar.lark'
    return Lark(_grammar_file.open().read())

_parser = get_parser()
_transformer = transformer.DicePoolTransformer()

def read_dice(string):
    "Read a dice pool from a string using standard dice notation."
    return _transformer.transform(_parser.parse(string))

def roll_dice(string):
    "Read in a dice pool from a string and roll it."
    return read_dice(string).roll()

def dice(sides, amount=1):
    "Create a simple dice pool"
    return pools.DiceTypePool(sides, amount)

def inspect(pool):
    "Inspect a pool for the values it can produce and their probabilities."
    return pool.values, {val: pool.prob(val) for val in pool.values}

def compare(*dpools):
    """
    Compare a group of pools on the values they can produce and their probabilities. Returns a
    dictionary from numbers to a list of numbers. The keys are the values that the pools together
    can produce, and the values are the probabilities that the pools will produce those values, in
    the same order as the input.
    """
    values = sorted(reduce(lambda p1, p2: p1.values.union(p2.values), dpools))
    return {val: [pool.prob(val) for pool in dpools] for val in values}
