"""
Task_9_1
Implement `swap_quotes` function which receives a string and replaces all " symbols with ' and vise versa.
The function should return modified string.

Note:
Usage of built-in or string replacing functions is required.
"""


def swap_quotes(some_string: str) -> str:
    """
    Replaces all " symbols with ' and vise versa.
    :paman some_string: string to change
    :return: changed string
    """
    l = some_string.split("'")
    string_result = '"'.join(part.replace('"',"'") for part in l) 
    return string_result

