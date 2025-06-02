
from diff.diff import xml_diff, text_diff
from utils.utils import write_output
import sys


def main():
    dir = "laws/samples/" + sys.argv[1].rstrip("/") + "/"
    old_file = dir + "old.xml"
    new_file = dir + "new.xml"

    xml_result = xml_diff(old_file, new_file)
    write_output(dir + "diff.xml", xml_result.__str__())

    text_result = text_diff(old_file, new_file)
    write_output(dir + "diff.html", text_result)


if __name__ == "__main__":
    main()
