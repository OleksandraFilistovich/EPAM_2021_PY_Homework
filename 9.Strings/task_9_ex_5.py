"""
Implement function count_letters, which takes string as an argument and
returns a dictionary that contains letters of given string as keys and a
number of their occurrence as values.

Example:
print(count_letters("Hello world!"))
Result: {'H': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

Note: Pay attention to punctuation.
"""


def count_letters(text: str) -> dict:
    """
    Counts how many times letters occur in given string.
    :param text: string
    :return: dictionary
    """
    result_dict = {}

    for char in text:
        if char.isalpha():
            if char in result_dict:
                result_dict[char] += 1
            else:
                result_dict[char] = 1
    return result_dict
