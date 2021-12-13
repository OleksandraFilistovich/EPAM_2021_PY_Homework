"""
Write a function converting a Roman numeral from a given string N into an Arabic numeral.
Values may range from 1 to 100 and may contain invalid symbols.
Invalid symbols and numerals out of range should raise ValueError.

Numeral / Value:
I: 1
V: 5
X: 10
L: 50
C: 100

Example:
N = 'I'; result = 1
N = 'XIV'; result = 14
N = 'LXIV'; result = 64

Example of how the task should be called:
python3 task_3_ex_2.py LXIV

Note: use `argparse` module to parse passed CLI arguments
"""
import argparse


def correct_characters(input_str):
    """
    Checks if input string contains valid characters.

    :param input_str: String with Roman number to check.
    :return: bool value of check.
    """
    if input_str == '':
        return False
    return all([ch in 'IVXLC' for ch in input_str])


def from_roman_numerals(number):
    """
    Transforms Roman number to Arabic.

    :param number: String with Roman number.
    :return: Arabic number as int.
    """
    if correct_characters(number):
        transform = {'I': 1,
                     'V': 5,
                     'X': 10,
                     'L': 50,
                     'C': 100}
        values = [transform[ch] for ch in number]

        result = sum(
            val if val >= next_val else -val
            for val, next_val in zip(values[:-1], values[1:])
        ) + values[-1]
        return result
    else:
        raise ValueError


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('number', type=str,
                        help='Roman number.')

    args = parser.parse_args()
    print(from_roman_numerals(args.number))


if __name__ == "__main__":
    main()
