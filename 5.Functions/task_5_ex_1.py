"""
Write 2 functions:
1. Function 'is_sorted', determining whether a given list of integer values of arbitrary length
is sorted in a given order (the order is set up by enum value SortOrder).
List and sort order are passed by parameters. Function does not change the array, it returns
boolean value.

2. Function 'transform', replacing the value of each element of an integer list with the sum
of this element value and its index, only if the given list is sorted in the given order
(the order is set up by enum value SortOrder). List and sort order are passed by parameters.
To check, if the array is sorted, the function 'is_sorted' is called.

Example for 'transform' function,
For [5, 17, 24, 88, 33, 2] and “ascending” sort order values in the array do not change;
For [15, 10, 3] and “ascending” sort order values in the array do not change;
For [15, 10, 3] and “descending” sort order the values in the array are changing to [15, 11, 5]

Note:
Raise TypeError in case of wrong function arguments data type;
"""

from enum import Enum


class SortOrder(Enum):
    ASC = "ascending"
    DESC = "descending"


def is_sorted(num_list, sort_order):
    """
    Function is determining whether a given list of integer values of arbitrary length
    is sorted in a given order (the order is set up by enum value SortOrder).

    :param num_list: list of integers to check whether or not they are sorted
    :param sort_order: sort order, element of SortOrder class
    :return: bool value is list sorted correctly or not
    """

    # if not isinstance(num_list, list) or sort_order is not SortOrder.ASC\
    #        or sort_order is not SortOrder.DESC:
    #    raise TypeError

    sort_type = (sort_order is SortOrder.DESC)
    sorted_list = sorted(num_list, reverse=sort_type)

    return sorted_list == num_list


def transform(num_list, sort_order):
    """
    Function is replacing the value of each element of an integer list with the sum
    of this element value and its index, only if the given list is sorted in the given order
    (the order is set up by enum value SortOrder).

    :param num_list: list of integers
    :param sort_order: sort order, element of SortOrder class
    :return:
    """

    if not is_sorted(num_list, sort_order):
        return num_list

    result = []
    for i in range(len(num_list)):
        result.append(i + num_list[i])

    return result
