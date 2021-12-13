"""Implement a function `most_common_words(file_path: str, top_words: int) -> list`
which returns most common words in the file.
<file_path> - system path to the text file
<top_words> - number of most common words to be returned

Example:

print(most_common_words(file_path, 3))
>>> ['donec', 'etiam', 'aliquam']
> NOTE: Remember about dots, commas, capital letters etc.
"""


def char_check(char):
    return char.isalpha() or char == ' '


def most_common_words(text, top_words):
    """
    Returns most common words in the file.
    :param text: system path to the text file
    :param top_words: number of words to find
    :return: list of words
    """
    words_occurance = {}
    words_list = []

    with open(text, 'r') as f:
        for line in f.readlines():
            alpha_line = ''.join(filter(char_check, line))
            words = alpha_line.split(' ')

            for word in words:
                words_occurance.setdefault(word, 0)
                words_occurance[word] += 1
            
        occurance_sorted = dict(sorted(words_occurance.items(), \
                                key=lambda item: item[1], \
                                reverse=True))

    for word in occurance_sorted.keys():
        top_words -= 1
        words_list.append(word)
        if top_words == 0:
            break
    
    return words_list
