"""
Implement function combine_dicts, which receives a changeable
number of dictionaries (keys - letters, values - integers)
and combines them into one dictionary.

Dict values should be summarized in case of identical keys.

Example:
dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

combine_dicts(dict_1, dict_2)
Result: {'a': 300, 'b': 200, 'c': 300}

combine_dicts(dict_1, dict_2, dict_3)
Result: {'a': 600, 'b': 200, 'c': 300, 'd': 100}
"""


def combine_dicts(*args):
    """
    Function  receives a changeable number of dictionaries
    and combines them into one dictionary.
    Dict values would be summarized in case of identical keys.

    :param args: changeable number of dictionaries (keys - letters, values - integers)
    :return: combined dictionary
    """

    result_dict = {}
    for dict in args:
        for key in dict:
            if key in result_dict:
                result_dict[key] += dict[key]
            else:
                result_dict[key] = dict[key]
    return result_dict

