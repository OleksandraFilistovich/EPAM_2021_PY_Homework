"""
Task04_6

Implement a function get_longest_word(s: str) -> str which returns the longest word in the given string.
The word can contain any symbols except whitespaces (`,\n,\tand so on).
If there are multiple longest words in the string with a same length return the word that occurs first.

Example: get_longest_word('Python is simple and effective!')
         #output: 'effective!'
         get_longest_word('Any pythonista like namespaces a lot.')
         #output: 'pythonista'

Note:
Raise ValueError in case of wrong data type
Usage of 're' library is prohibited
"""


def get_longest_word(str_to_parse: str) -> str:
    """
    Function returns the longest word in the given string. The word can contain any symbols except whitespaces.
    :param str_to_parse: string to find tha largest word in
    :return: first longest word in the given string
    """
    if isinstance(str_to_parse, str):
        list_words = str_to_parse.split()
        list_length = [len(word) for word in list_words]
        index_of_max = list_length.index(max(list_length))
        return list_words[index_of_max]
    else:
        raise ValueError
