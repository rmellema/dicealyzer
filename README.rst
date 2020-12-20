==========
dicealyzer
==========
dicealyzer is a python library for rolling and analyzing dice. The goal of the project is
to allow people the easily define new pools of dice using `standard dice notation`, and to
calculate probabilities over them.

Currently supported are:

* Pools of dice of one type: `d6`, `2d20`;
* Simple arithmatic: `1d4 + 3`, `3d6 * 5`;
* Dropping the highest/lowest dice: `4d6-L`, `2d20-H`, `3d100l1`, `3d100k1`;
* And combinations of the above.

.. _standard dice notation: https://en.wikipedia.org/wiki/Dice_notation
