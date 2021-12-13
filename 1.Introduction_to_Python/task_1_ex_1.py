"""01-Task1-Task1
Write a Python-script that performs simple arithmetic operations: '+', '-', '*', '/'. The type of operator and
data are set on the command line when the script is run.
The script should be launched like this:
$ python my_task.py 1 * 2

Notes:
For other operations need to raise NotImplementedError.
Do not dynamically execute your code (for example, using exec()).
Use the argparse module to parse command line arguments. Your implementation shouldn't require entering any
parameters (like -f or --function).
"""

import argparse


def calculate(args):
    variables = vars(args)
    ind = '+-*/'.find(variables['operator'])
    if ind == -1:
        raise NotImplementedError("Invalid operator value. Must be + - * or /")
    elif ind == 0:
        res = variables['x'] + variables['y']
    elif ind == 1:
        res = variables['x'] - variables['y']
    elif ind == 2:
        res = variables['x'] * variables['y']
    else:
        if variables['y'] == 0:
            raise ZeroDivisionError("Denominator can't be zero.")
        res = variables['x'] / variables['y']
    return res


def main():
    parser = argparse.ArgumentParser(description='Process some operation with integers.')

    parser.add_argument('x', type=float)
    parser.add_argument('operator', type=str)
    parser.add_argument('y', type=float)

    args = parser.parse_args()
    print(calculate(args))


if __name__ == '__main__':
    main()
