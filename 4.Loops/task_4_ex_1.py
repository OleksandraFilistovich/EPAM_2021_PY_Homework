"""04 Task 1.1
Implement a function which receives a string and replaces all " symbols with ' and vise versa. The
function should return modified string.
Usage of any replacing string functions is prohibited.
"""


def swap_quotes(string: str) -> str:
    """
    Receives a string and replaces all " symbols with ' and vise versa
    :param string: string to be modified
    :return: modified string
    """
    result_string = ''
    for char in string:
        if char == '"':
            result_string += "'"
        elif char == "'":
            result_string += '"'
        else:
            result_string += char
    return result_string

