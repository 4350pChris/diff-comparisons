from utils.utils import get_proper_path
from difflib import HtmlDiff
from graphtage import xml, printer


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


def xml_diff(left: str, right: str, out_stream=None):
    from_tree = xml.build_tree(get_proper_path(left))
    to_tree = xml.build_tree(get_proper_path(right))
    diff = from_tree.diff(to_tree)
    formatter = xml.XMLFormatter()
    formatter.print(printer.HTMLPrinter(out_stream=out_stream), diff)
