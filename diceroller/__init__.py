"""
This module provides ways to define and combine pools of dice so they can be analyzed.
"""
import pathlib
from lark import Lark

from . import pools, transformer
__VERSION__ = '0.0.1'

_grammar_file = pathlib.Path(__file__).parent.absolute() / 'grammar.lark'
_parser = Lark(_grammar_file)
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
