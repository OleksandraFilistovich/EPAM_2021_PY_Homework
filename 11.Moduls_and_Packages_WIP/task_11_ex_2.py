"""
Implement a decorator remember_result which remembers last result of function it decorates
and prints it before next call.

@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += str(item)
    print(f"Current result = '{result}'")
    return result

sum_list("a", "b")
>>> "Last result = 'None'"
>>> "Current result = 'ab'"

sum_list("abc", "cde")
>>> "Last result = 'ab'"
>>> "Current result = 'abccde'"

sum_list(3, 4, 5)
>>> "Last result = 'abccde'"
>>> "Current result = '345'"
"""

memory = 'None'


def remember_result(fn):
    def wrapper(*args):
        global memory
        print(f"Last result = '{memory}'")
        memory = fn(*args)
        return memory
    return wrapper


@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += str(item)
    print(f"Current result = '{result}'")
    return result
