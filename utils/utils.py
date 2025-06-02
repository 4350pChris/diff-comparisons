from os import path
import sys


def get_proper_path(file: str) -> str:
    """
    Returns the proper path of the file no matter where we launched the script from
    """
    return path.join(path.dirname(sys.argv[0]), file)


def write_output(file: str, content: str):
    """
    Writes the content to the file.
    """
    with open(get_proper_path(file), 'w', encoding='utf-8') as f:
        f.write(content)
