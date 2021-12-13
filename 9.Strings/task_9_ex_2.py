"""
Write a function that checks whether a string is a palindrome or not.
Return 'True' if it is a palindrome, else 'False'.

Note:
Usage of reversing functions is required.
Raise ValueError in case of wrong data type

To check your implementation you can use strings from here
(https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).
"""


def is_palindrome(test_string: str) -> bool:
    """
    Checks whether a given string is a palindrome or not. Functions ignores special characters, whitespaces and different cases.
    :param test_string: string
    :return: 'True' if test_string is palindrome, else 'False'
    """
    test_string = test_string.lower()
    normalized_string = ''

    if not isinstance(test_string, str):
        raise ValueError

    for char in test_string:
        if char.isalnum():
            normalized_string += char

    if normalized_string == ''.join(reversed(normalized_string)):
        return True
    else:
        return False
