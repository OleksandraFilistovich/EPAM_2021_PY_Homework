"""
Task04_1_7
Implement a function foo(List[int]) -> List[int] which, given a list of integers, returns a new  or modified list
in which every element at index i of the new list is the product of all the numbers in the original array except the one at i.
Example:
`python

foo([1, 2, 3, 4, 5])
[120, 60, 40, 30, 24]

foo([3, 2, 1])
[2, 3, 6]`
"""

from typing import List


def multiply_except_index(l, ind):
    """
    Function returns multiplication of all elements of the list, except the element with given index.

    :param l: list of integers
    :param ind: index of excluded element
    :return: resulting int
    """
    multi = 1
    for i in range(len(l)):
        if i != ind:
            multi *= l[i]
    return multi


def product_array(num_list: List[int]) -> List[int]:
    """
    Function which, given a list of integers, returns a new list
    in which every element at index i of the new list is the product
    of all the numbers in the original array except the one at i.

    :param num_list: list of integers
    :return: list of integers
    """
    multiplied = 1
    result = []

    for i in num_list:
        multiplied *= i

    if multiplied != 0:
        for i in num_list:
            result.append(int(multiplied / i))
    else:
        for i in range(len(num_list)):
            result.append(multiply_except_index(num_list, i))
    return result
