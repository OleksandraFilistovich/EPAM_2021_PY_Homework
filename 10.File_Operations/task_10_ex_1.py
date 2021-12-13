"""
Implement a function `sort_names(input_file_path: str, output_file_path: str) -> None`, 
which sorts names from `file_path` and write them to a new file `output_file_path`. 
Each name should start with a new line as in the following example:
Example:

Adele
Adrienne
...
Willodean
Xavier
"""


def sort_names(input_file_path: str, output_file_path: str) -> None:
    """
    Sorts names from `input_file_path` and write them to a new file `output_file_path`.
    Each name should start with a new line.
    :param input_file_path: system path to the text file
    :param output_file_path: system path to the text file
    :return: None
    """
    names = []

    with open(input_file_path, 'r') as f:
        not_normalized_names = f.readlines()
        names = [name.strip() for name in not_normalized_names]
        names.sort()
    
    with open(output_file_path, 'w') as f:
        f.write('\n'.join(names))

sort_names('text_1.txt','text_2.txt')