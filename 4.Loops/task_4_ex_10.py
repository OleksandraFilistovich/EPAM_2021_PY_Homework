"""
Create a function sum_binary_1 that for a positive integer n
calculates the result value, which is equal to the sum of the
“1” in the binary representation of n otherwise, returns None.

Example,
n = 14 = 1110 result = 3
n = 128 = 10000000 result = 1
"""


def sum_binary_1(n: int):
    """
    Function that for a positive integer n
    calculates the result value, which is equal to the sum of the
    “1” in the binary representation of n otherwise, returns None.

    :param n: positive integer
    :return: sum of binary '1'
    """

    sum = 0

    if isinstance(n, int) and n >= 0:
        for i in bin(n)[2:]:
            sum += int(i)

    if sum:
        return sum
    else:
        return None
