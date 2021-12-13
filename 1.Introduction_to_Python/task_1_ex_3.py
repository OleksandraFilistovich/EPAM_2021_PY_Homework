""" Write a Python-script that determines whether the input string is the correct entry for the
'formula' according EBNF syntax (without using regular expressions).
Formula = Number | (Formula Sign Formula)
Digit = '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
Number = Digit{Digit}
Sign = '+' | '-'
Input: string
Result: (True / False, The result value / None)

Example,
user_input = '1+2+4-2+5-1' result = (True, 9)
user_input = '123' result = (True, 123)
user_input = '-123' result = (False, None)
user_input = 'hello+12' result = (False, None)
user_input = '2++12--3' result = (False, None)
user_input = '' result = (False, None)

Example how to call the script from CLI:
python task_1_ex_3.py 1+5-2

Hint: use argparse module for parsing arguments from CLI
"""

# import re
import argparse


def correct_characters(input_str):
    if input_str == '':
        return False
    return all([ch in '0123456789+-' for ch in input_str])


def replace_digits(input_str):
    result_str = ''
    for ch in input_str:
        if ch.isdigit():
            result_str += ','
        else:
            result_str += ch
    return result_str


def correct_formula(input_str):
    if not correct_characters(input_str):
        return False
    elif not input_str[0].isdigit() \
            or not input_str[-1].isdigit():
        return False
    result_str = replace_digits(input_str)
    if any([len(block) > 1 for block in result_str.split(',')]):
        return False
    return True


def check_formula(formula):
    """Check is formula valid or not and calculates it."""

    formula = ''.join(formula).replace(' ', '')

    if correct_formula(formula):
        return True, eval(formula)
    else:
        return False, None


    # hard coded
    """flag = False
    res = None

    if formula:
        if formula[0].isdigit() and formula[-1].isdigit():
            if formula.find('++') == -1 and formula.find('--') == -1 and formula.find('+-') == -1 and formula.find('-+') == -1 and formula.find('=') == -1:
                try:
                    res = eval(formula)
                    flag = True
                except:
                    flag = False
        
    return flag, res"""

    # regular expressions
    """match = re.search(r'^[0-9][-+0-9]+[0-9]', formula)
    match_repeat = re.search(r'[+-][+-]', formula)

    if match is not None and match_repeat is None:
        if match.group() == formula:
            try:
                res = eval(formula)
                flag = True
            except:
                flag = False

    return flag, res"""


def main():
    parser = argparse.ArgumentParser(description='Check some formula.')
    parser.add_argument('user_input', type=str, nargs='+')

    args = parser.parse_args()
    print(check_formula(args.user_input))


if __name__ == '__main__':
    main()
