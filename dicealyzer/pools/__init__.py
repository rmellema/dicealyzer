"""
A module to represent dice pools before they are rolled.

A dice pool is a collection of dice or numbers that can be combined in various ways, and rolled
later on. The package also offers a few ways to analyse the values that it can roll and how likely
that is.

Dice pools are assumed to produce numbers, but that is only necessary if they are combined with the
standard dice pools defined in this package. Otherwise, you can use any custom type, as long as it
is discrete.

This module exports:

* The base class for all dice pools, :py:class:`~dicealyzer.pools.base.AbstractDicePool`
* Pools of :py:class:`one type of dice <dicealyzer.pools.dice.DiceTypePool>`
* Pools for :py:class:`dropping and keeping dice <dicealyzer.pools.dice.DiceDropPool>`
* Pools for :py:class:`combining other pools using binary operators <.BinaryOperatorPool>`

It also allows dice pools to be combined with the python operators ``+``, ``-``, ``*``, and ``/``.
"""
from .base import AbstractDicePool
from .dice import DiceTypePool, DiceDropPool
from .operator import *
