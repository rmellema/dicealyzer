"""
This module defines the command line interface parts of dicealyzer.
"""
import argparse
import dicealyzer
from tabulate import tabulate

def roll(args):
    value, rolls = dicealyzer.roll_dice(args.dice)
    print("Rolled {}: {}".format(args.dice, value))
    print("Rolls: {}".format(rolls))

def compare(args):
    pools = map(dicealyzer.read_dice, args.dice)
    compared = dicealyzer.compare(*pools)
    print(tabulate([[val] + compared[val] for val in compared], headers= [''] + args.dice))

def get_arg_parser():
    parser = argparse.ArgumentParser(usage="A command line utility for rolling and analysing dice.")
    sub_parsers = parser.add_subparsers()
    roll_parser = sub_parsers.add_parser("roll", help="Rolls a given dice")
    roll_parser.add_argument("dice", help="The dice to roll")
    roll_parser.set_defaults(func=roll)
    compare_parser = sub_parsers.add_parser("compare", help="Compare various dice with each other")
    compare_parser.add_argument("dice", nargs='+',
                                help="The dice to compare against each other")
    compare_parser.set_defaults(func=compare)
    return parser

def main():
    args = get_arg_parser().parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
