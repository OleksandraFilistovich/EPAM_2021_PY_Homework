"""
Implement a function `split_by_index(string: str, indexes: List[int]) -> List[str]`
which splits the `string` by indexes specified in `indexes`. 
Only positive index, larger than previous in list is considered valid.
Invalid indexes must be ignored.

Examples:
```python
>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 8, -4, 0, "u", 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

>>> split_by_index("no luck", [42])
["no luck"]
```
"""


def split_by_index(string, indexes):
    """
    Function splits given string by list of indexes. Ignores non-positive or smaller than previous indexes.
    :param string: string to split by indexes
    :param indexes: list of indexes
    :return: list of splitted strings
    """
    result_strings = []
    prev_index = 0

    for index in indexes:
        if isinstance(index, int) and index > prev_index:
            result_strings.append(string[prev_index:index])
            prev_index = index

    if prev_index < len(string):
        result_strings.append(string[prev_index:])
    return result_strings

