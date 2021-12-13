"""
Task 04-Task 1.8
Implement a function which takes a list of elements and returns a list of tuples containing pairs of this elements.
Pairs should be formed as in the example. If there is only one element in the list return `None`
instead.
Using zip() is prohibited.

Examples:
>>> get_pairs([1, 2, 3, 8, 9])
[(1, 2), (2, 3), (3, 8), (8, 9)]

>>> get_pairs(['need', 'to', 'sleep', 'more'])
[('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]

>>> get_pairs([1])
None
"""


def get_pairs(lst: list) -> list:
    """
    Function which takes a list of elements and returns a list of tuples containing pairs of this elements.
    Grouped by two: i-element and (i+1)-element with i-step == 1.

    :param lst: list
    :return: list of tuples
    """

    if len(lst) == 1:
        return None

    tuple_list = [(lst[0], lst[1])]
    for i in range(2, len(lst)):
        tuple_list.append((lst[i-1], lst[i]))
    return tuple_list
