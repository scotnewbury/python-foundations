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


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(read_text(sys.argv[1]))
