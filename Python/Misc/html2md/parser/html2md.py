#!/home/hmchen/.venvs/html2md-Z6Rs3Moi/bin/python3

import argparse
import os

DEFAULTDIR = "../working"
DEFAULTFILE = "reading_in.md"


def check_exist(folder, files):
    """check files exist in the given dir"""
    base_dir = os.path.dirname(os.path.realpath(__file__))
    not_exist = [
        fname
        for fname in files
        if not (
            (os.path.isfile(os.path.join(os.path.join(base_dir, folder), fname)))
            and (os.path.splitext(fname)[1] == ".md")
        )
    ]
    print(not_exist)

    if not_exist:
        print(
            f"\nInput file(s) neither existing nor markdown file(s) in {folder} dir:\n\t{files}\n"
        )
        exit()

    return True


def get_md_files():
    """Parsing the command line args to read in files and target file path/name"""
    parser = argparse.ArgumentParser(
        description="Convert embedded HTML figures and tables code to markdown syntax"
    )
    parser.add_argument(
        "inputs", nargs="*", default=[DEFAULTFILE], help="Markdown files to process"
    )
    parser.add_argument(
        "-d",
        "--dir",
        default=DEFAULTDIR,
        help="The folder to retrieve markdown files, the path also used to process local diagrams",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="reading.md",
        help="Output markdown file for pandoc to process",
    )

    args = parser.parse_args()

    # generate list of read in markdown files
    inputs = []

    check_exist(args.dir, args.inputs)
    exit()

    for fname in inputs:
        inputs.append(os.path.join(args.dir, fname))

    return (os.path.join("../working", args.output), inputs)


if __name__ == "__main__":
    outfile, md_files = get_md_files()
    print(md_files)
    print(outfile)
