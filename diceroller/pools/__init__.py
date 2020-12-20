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
