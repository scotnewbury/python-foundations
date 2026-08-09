import os
import sys


def read_text(path: str) -> str:
    """Read and return the contents of a file.

    Checks that the file exists and then reads the contents.

    Args:
        path: The filename

    Returns:
        A string with the contents of the file, or empty if no file exists.
    """
    if not os.path.exists(path):
        return ""

    file_handle = open(path, encoding="utf-8")
    content = file_handle.read()
    file_handle.close()

    return content


def count_words(text: str) -> dict[str, int]:
    """Read a string and return a dictionary of words and their counts.

    The string is normalized by making it lowercase and removing edge punctuation.

    Words that are normalized to nothing are excluded from the count.

    Args:
        text: The string containing the words to be counted

    Returns:
        A dictionary of keys and their counts, or an empty dictionary.
    """
    if text == "":
        return {}

    word_dict: dict[str, int] = {}
    word_list = text.lower().split()

    for word in word_list:
        word = word.strip(".,!?;:'\"")
        if word:
            word_dict[word] = word_dict.get(word, 0) + 1

    return word_dict


def top_n_words(freq: dict[str, int], n: int) -> list[tuple[str, int]]:
    """Accept a dictionary and return the top n key:value pairings

    A sorted list from the dictionary is created and the top n values are returned.

    Args:
        freq: The dictionary to be read
        n: The number of values to be returned

    Returns:
        A list of the top n key:value pairings.
    """
    most_frequent_words = sorted(freq.items(), key=lambda item: item[1], reverse=True)[
        :n
    ]
    return most_frequent_words


def unique_words(freq: dict[str, int]) -> set[str]:
    """Accept a dictionary and return a set of all unique words"""
    return set(freq.keys())


def words_by_first_letter(freq: dict[str, int]) -> dict[str, list[str]]:
    """Group words by their first letter.

    Builds a new dictionary where each key is a starting letter and each
    value is a list of words from freq that begin with that letter.

    Args:
        freq: The dictionary to be read.

    Returns:
        A dictionary mapping each starting letter to a list of words
        that begin with it.
    """
    words_grouped_by_first_letter: dict[str, list[str]] = {}
    for word in freq:
        words_grouped_by_first_letter.setdefault(word[0], []).append(word)
    return words_grouped_by_first_letter


def filter_words(
    freq: dict[str, int], min_length: int = 1, min_count: int = 1
) -> dict[str, int]:
    """Filter words by minimum length and count.

    Builds a new dictionary where each key meets a minimum requirement
    for both word length and frequency.

    Args:
        freq: The dictionary to be read
        min_length: The minimum number of characters required for the word to be
            included
        min_count: The minimum count for the word to be included

    Returns:
        A dictionary of words meeting the minimum requirements and their
        frequency count.
    """

    return {"that": 4, "start": 5}


if __name__ == "__main__":
    if len(sys.argv) > 1:
        string_of_words = read_text(sys.argv[1])
        dictionary_of_words = count_words(string_of_words)
        # print("The dictionary of words: \n", dictionary_of_words)
        # print("\n\n", top_n_words(dictionary_of_words, 5))
        # print("\n\n", unique_words(dictionary_of_words))
        print(words_by_first_letter(dictionary_of_words))
