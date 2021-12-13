"""
Implement a bunch of functions which receive a changeable number of strings and return next
parameters:
1) characters that appear in all strings
2) characters that appear in at least one string
3) characters that appear at least in two strings
  Note: raise ValueError if there are less than two strings
4) characters of alphabet, that were not used in any string
    Note: use `string.ascii_lowercase` for list of alphabet letters

Note: raise TypeError in case of wrong data type

Examples,
```python
test_strings = ["hello", "world", "python", ]
print(chars_in_all(*test_strings))
>>> {'o'}
print(chars_in_one(*test_strings))
>>> {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
print(chars_in_two(*test_strings))
>>> {'h', 'l', 'o'}
print(not_used_chars(*test_strings))
>>> {'q', 'k', 'g', 'f', 'j', 'u', 'a', 'c', 'x', 'm', 'v', 's', 'b', 'z', 'i'}
"""


import string


def dict_of_occurrence(*strings):
    """
    Counts number of strings charecters occurs in.
    :param strings: unknown number of strings
    :return: dictionary
    """
    result_dict = {}

    for s in strings:
        for char in set(s):
            if char in result_dict:
                result_dict[char] += 1
            else:
                result_dict[char] = 1
    return result_dict


def chars_in_all(*strings):
    """
    Returns characters that appear in all strings.
    :param strings: unknown number of strings
    :return: set of characters
    """
    occurrence = dict_of_occurrence(*strings)
    result_set = set()
    n = len(strings)

    for char, number in occurrence.items():
        if number == n:
            result_set.add(char)
    return result_set


def chars_in_one(*strings):
    """
    Returns characters that appear in at least one string.
    :param strings: unknown number of strings
    :return: set of characters
    """
    occurrence = dict_of_occurrence(*strings)
    result_set = set()

    for char, number in occurrence.items():
        if number >= 1:
            result_set.add(char)
    return result_set


def chars_in_two(*strings):
    """
    Returns characters that appear at least two string.
    :param strings: unknown number of strings
    :return: set of characters
    """
    occurrence = dict_of_occurrence(*strings)
    result_set = set()

    for char, number in occurrence.items():
        if number >= 2:
            result_set.add(char)
    return result_set


def not_used_chars(*strings):
    """
    Returns characters of alphabet, that were not used in any string.
    :param strings: unknown number of strings
    :return: set of characters
    """
    occurrence = dict_of_occurrence(*strings)
    result_set = set()
    for char in string.ascii_lowercase:
        if char not in occurrence:
            result_set.add(char)
    return result_set
