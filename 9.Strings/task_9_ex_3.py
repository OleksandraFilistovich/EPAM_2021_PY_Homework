"""
Implement a function get_longest_word(s: str) -> str which returns the
longest word in the given string. The word can contain any symbols
except whitespaces (`,\n,\t and so on). If there are multiple longest
words in the string with a same length return the word that occurs first.

Example:
get_longest_word('Python is simple and effective!')
#output: 'effective'
get_longest_word('Any pythonista like namespaces a lot.')
#output: 'pythonista'

Note:
Raise ValueError in case of wrong data type
Usage of 're' library is required.
"""


import re


def get_longest_word(text: str) -> str:
    """
    Returns the longest word in the given string.
    :param text: string
    :return: first longest word
    """
    if not isinstance(text, str):
        raise ValueError
    
    if not text:
        return ''
    words = re.findall(r"\S+", text)
    lengths = {len(word):word for word in words[::-1]}
    longest = lengths[max(lengths.keys())]

    return longest
