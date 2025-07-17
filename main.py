
from diff.diff import xml_diff, text_diff
from utils.utils import write_output
import sys

DIR_PREFIX = "laws/samples/"


def run_comparision(path: str):
    """
    Runs the comparison for the given path.
    """
    dir = DIR_PREFIX + path.rstrip("/") + "/"
    old_file = dir + "old.xml"
    new_file = dir + "new.xml"

    diff = xml_diff(old_file, new_file)
    write_output(dir + "xml_diff.html", diff)

    text_result = text_diff(old_file, new_file)
    write_output(dir + "text_diff.html", text_result)


def recurse_dir(path: str):
    """
    Go through all directories under the given path and run the comparison for each dir that contains old.xml and new.xml files.
    """
    import os
    for root, _, files in os.walk(path):
        if "old.xml" in files and "new.xml" in files:
            without_prefix = root.replace(DIR_PREFIX, "")
            run_comparision(without_prefix)


def main():
    path_arg = sys.argv[1] if len(sys.argv) > 1 else "all"
    if path_arg == "all":
        recurse_dir(DIR_PREFIX)
    else:
        # run comparison for the specified path
        run_comparision(path_arg)


if __name__ == "__main__":
    main()
