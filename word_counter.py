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


# print(count_words("The cat didn't sat on the mat, mat"))

print("Second test: ", count_words(".,!?;:'\""))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(read_text(sys.argv[1]))
