"""
Task04_3

Implement a function which works the same as str.split

Note:
Usage of str.split method is prohibited
Raise ValueError in case of wrong data type
"""


def split_alternative(str_to_split: str, delimiter: str) -> list:
    """
    Function which splits string by delimiter and returns list of substrings.
    :param str_to_split: string to split by delimiter
    :param delimiter: string with delimiter
    :return: list of delimited strings
    """
    result_strings = []

    if not isinstance(str_to_split, str) or not isinstance(delimiter, str):  # check for given value type
        raise ValueError

    del_len = len(delimiter)
    prev_index = - del_len
    index = str_to_split.find(delimiter)
    while index != -1:
        result_strings.append(str_to_split[prev_index+del_len:index])
        prev_index = index
        index = str_to_split.find(delimiter, prev_index + del_len)

    if not result_strings:  # if no delimiter was found
        result_strings.append(str_to_split)
    else:
        result_strings.append(str_to_split[prev_index+del_len:])
    return result_strings
