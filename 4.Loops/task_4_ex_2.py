"""
Task04_1_2
Write `is_palindrome` function that checks whether a string is a palindrome or not
Returns 'True' if it is palindrome, else 'False'

To check your implementation you can use strings from here
(https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).

Note:
Usage of any reversing functions is prohibited.
The function has to ignore special characters, whitespaces and different cases
Raise ValueError in case of wrong data type
"""


def is_palindrome(test_string: str) -> bool:
    """
    Checks whether a given string is a palindrome or not. Functions ignores special characters, whitespaces and different cases.
    :param test_string: string with possible palindrome
    :return: 'True' if test_string is palindrome, else 'False'
    """
    test_string = test_string.lower()
    normalized_string = ''
    if not isinstance(test_string, str):  # check for given value type
        raise ValueError

    for char in test_string:  # remove ignored symbols
        if char.isalnum():
            normalized_string += char

    if normalized_string == normalized_string[::-1]:
        return True
    else:
        return False
