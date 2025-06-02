from xmldiff import main, formatting
from formatter.html_formatter import HTMLFormatter
from utils.utils import get_proper_path
from difflib import HtmlDiff


def read_file_and_split(file: str) -> list[str]:
    """
    Reads a file and splits it into lines.
    """
    with open(get_proper_path(file), 'r', encoding='utf-8') as f:
        return f.read().splitlines()


def text_diff(left: str, right: str):
    left_lines = read_file_and_split(left)
    right_lines = read_file_and_split(right)

    return HtmlDiff(wrapcolumn=60).make_file(
        left_lines,
        right_lines,
        context=True,
        numlines=1,
    )


def make_formatter(klass: type[formatting.XMLFormatter]) -> formatting.XMLFormatter:
    """
    Returns a formatter instance of the given class.
    """
    return klass()


def xml_diff(left: str, right: str):
    formatter = make_formatter(HTMLFormatter)
    return main.diff_files(
        get_proper_path(left),
        get_proper_path(right),
        formatter=formatter,
        diff_options={
            'fast_match': True,
        }
    )
