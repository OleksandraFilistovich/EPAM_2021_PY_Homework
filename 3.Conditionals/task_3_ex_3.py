
"""
Write a Python-script that:
1. Searches for files by a given pattern (pattern can include: *, ?)
2. Displays the search result
3. Gets access rights for each file that is found and displays the result

The script should have 2 obligatory functions:
- finder - a generator function searches for files by a given pattern
 in a given path returns an absolute path of a found file.
- display_result - displays founded files and files' permission
by a given list of absolute paths (You can find an example below).

Example call:
python task_3_ex_3.py /usr/bin -p '?ython*'

Example result:
...
/usr/bin/python3.6m -rwxr-xr-x
/usr/bin/python3.7m -rwxr-xr-x
Found 12 file(s).

Note: use of glob module is prohibited.

Hint: use os.walk, stat, fnmatch
"""
import os
import argparse
import stat
import fnmatch


def octal_to_string(octal):
    result = "-"
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for digit in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if digit >= value:
                result += letter
                digit -= value
            else:
                result += '-'
    return result


def finder(path, pattern):
    """Searches for files by a given pattern.

    :param path: Absolute path for searching.
    :param pattern: Can consist *, ?.
    :return: absolute path of found file.
    """
    tree = os.walk(path)

    for branch in tree:
        directory, catalogs, files = branch
        for file in fnmatch.filter(files, pattern):
            yield directory + '/' + file


def display_result(file_paths):
    """Displays founded file paths and file's permissions."""
    count = 0
    for file_path in file_paths:
        count += 1
        permissions, *other  = os.stat(file_path)
        permission = octal_to_string(oct(permissions)[-3:])
        print(file_path, permission)
    print(f'Found {count} file(s).')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str,
                        help='Absolute path to desired directory.')
    parser.add_argument('-p', type=str,
                        help='Pattern for files.')

    args = parser.parse_args()

    display_result(finder(args.path, args.p))

if __name__ == '__main__':
    main()
