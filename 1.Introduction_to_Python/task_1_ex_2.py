"""01-Task1-Task2
Write a Python-script that performs the standard math functions on the data. The name of function and data are
set on the command line when the script is run.
The script should be launched like this:
$ python my_task.py add 1 2

Notes:
Function names must match the standard mathematical, logical and comparison functions from the built-in libraries.
The script must raises all happened exceptions.
For non-mathematical function need to raise NotImplementedError.
Use the argparse module to parse command line arguments. Your implementation shouldn't require entering any
parameters (like -f or --function).
"""
import operator
import math
import argparse


def calculate(operation, args):
    not_implemented = False

    try:
        if hasattr(operator, operation):
            res = getattr(operator, operation)(*args)
        elif hasattr(math, operation):
            res = getattr(math, operation)(*args)
        else:
            if len(args) == 1:
                res = eval(operation + '(' + str(args[0]) + ')')
            else:
                res = eval(str(args[0]) + operation + str(args[1]))
    except KeyError:
        not_implemented = True

    if not_implemented:
        raise NotImplementedError

    return res


def main():
    parser = argparse.ArgumentParser(description='Process some operation with integers.')

    parser.add_argument('operator', type=str)
    parser.add_argument('args', type=float, default=None, nargs='+')

    values = vars(parser.parse_args())
    print(calculate(values['operator'], values['args']))


if __name__ == '__main__':
    main()
