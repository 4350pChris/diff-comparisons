
from diff.diff import xml_diff, text_diff
from utils.utils import write_output
import sys


def main():
    dir = "laws/samples/" + sys.argv[1].rstrip("/") + "/"
    old_file = dir + "old.xml"
    new_file = dir + "new.xml"

    with open(dir + "xml_diff.html", "w", encoding="utf-8") as xml_out_stream:
        xml_diff(old_file, new_file, xml_out_stream)

    text_result = text_diff(old_file, new_file)
    write_output(dir + "text_diff.html", text_result)


if __name__ == "__main__":
    main()
