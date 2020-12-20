Dice notation
=============
This page describes the used notation in detail, based on the lark grammar. The point of
the notation is to stay as close to the standard `dice notation` as possible. However, as
this notation is not entirely standard we had to make some choices. Furthermore, to make
it easier to work with, this notation ignores whitespace.

The base unit of the notation is writing down dice themselves. These are written as
``A d S`` or ``A D S`` where ``A`` is the number of dice to roll and ``S`` is the number of
sides on the dice. Both ``A`` and ``S`` need to be integers. When it is 1, the ``A`` can
be left off. So for example, a standard six sided dice is written as ``d6``, and 3 of them
is written as ``3d6``. When you specify multiple dice, their values are added together for
further calculations.

The notation can deal with dropping the lowest or highest rolled values. Keeping the
lowest values works by adding ``l N`` to the dice, where ``l`` stands for lowest, and ``N``
is the number of dice to keep. So ``4d20l2`` rolls 4 20 sided dice, and keeps the lowest
2 for further calculations. If you only want to drop 1 die, ``-H`` (minus highest) can be
used instead. Thus ``4d6-H`` rolls 4 6 sided dice, and keeps the lowest 3, the same as
``4d6l3``.

Similarly, you can also only keep the highest values. This can be done by adding ``k N`` or
``h N`` to the dice, where ``k`` stands for "keep", ``h`` for "highest", and ``N`` is the
number of dice to keep. If you only want to drop the lowest die, you can add ``-L`` (minus
lowest) to the dice instead. So ``4d6-L`` rolls 4 six-sided die, and keeps the highest
4, same as ``4d6k3``.

You can also add multiple dice pools together, subtract them, multiply them, and divide
them. This works with the usual operators ``+``, ``-``, ``*``, and ``/``. Operator
precedence is also as normal, so ``*`` and ``/`` bind stronger than ``+`` and ``-``. You
can use parenthesis (``(`` and ``)``) to influence how the operators are read in.

In order to make arithmatic easier, dicealyzer can also read in integers. This makes it
possible to write expressions such as ``(2d6 + 6) * 5``, which rolls 2 6 sided dice,
adds 6 to the result, and multiplies it by 5.

.. _dice notation: https://en.wikipedia.org/wiki/Dice_notation
