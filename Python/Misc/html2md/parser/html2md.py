#!/home/hmchen/.venvs/html2md-Z6Rs3Moi/bin/python3

import argparse
import os
import sys

from bs4 import BeautifulSoup

# add the Python path at runtime
base_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(1, base_dir)

from parse_fig import replace_fig_tags
from parse_tbl import replace_tbl_tags

DEFAULTDIR = "../working"
DEFAULTOUT = "reading.md"


def check_exist(folder: str, files: str) -> bool:
    """check files exist in the given dir"""

    not_exist = [
        fname
        for fname in files
        if not (
            (os.path.isfile(os.path.join(os.path.join(base_dir, folder), fname)))
            and (os.path.splitext(fname)[1] == ".md")
        )
    ]

    if not_exist:
        print(
            f"\nInput file(s) neither existing nor markdown file(s) in {folder} dir:\n\t{files}\n"
        )
        exit()

    return True


def get_md_files() -> (str, str):
    """Parsing the command line args to read in files and target file path/name"""
    parser = argparse.ArgumentParser(
        description="Convert embedded HTML figures and tables code to markdown syntax"
    )
    parser.add_argument("inputs", nargs="*", help="Markdown files to process")
    parser.add_argument(
        "-d",
        "--dir",
        default=DEFAULTDIR,
        help="The folder to retrieve markdown files, the path also used to process local diagrams",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=os.path.join(DEFAULTDIR, DEFAULTOUT),
        help="Output markdown file for pandoc to process",
    )

    args = parser.parse_args()

    # generate list of read in markdown files
    input_files = []

    if not args.inputs:
        # read all markdown file in the given directory
        if not os.path.exists(os.path.join(base_dir, args.dir)):
            print(f"No such directory {args.dir} exists!")
            exit()
        dir_lst = os.listdir(os.path.join(base_dir, args.dir))
        inputs = [
            md_file for md_file in dir_lst if (os.path.splitext(md_file)[1] == ".md")
        ]
    else:
        check_exist(args.dir, args.inputs)
        inputs = args.inputs

    for fname in inputs:
        input_files.append(os.path.join(os.path.join(base_dir, args.dir), fname))

    if args.output != os.path.join(DEFAULTDIR, DEFAULTOUT):
        return (
            os.path.join(os.path.join(os.path.join(base_dir, DEFAULTDIR), args.output)),
            input_files,
        )
    else:
        return (
            os.path.join(os.path.join(base_dir, os.path.join(DEFAULTDIR, DEFAULTOUT))),
            input_files,
        )


def parse_tags(outfile: list, md_files: list) -> str:
    """parsing embedded html tags to relative markdown syntax

    Args:
        outfile (lst): output filename
        md_files (lst): [md_file1, md_file2, ...]

    Returns:
        fd: file descriptor of output filename
    """
    for md_file in md_files:
        with open(md_file, "r", encoding="utf-8") as md_fd:
            soup = BeautifulSoup(md_fd.read(), "html.parser")
            print(f"\n\nhtml2md****************************\n\n{soup}\n")
            soup = replace_fig_tags(soup, os.path.basename(md_file))
            soup = replace_tbl_tags(soup)

            # write_outfile(outfile, soup)
            print(f"\n\nhtml2md----------------------------\n\n{soup}\n")

    return outfile


if __name__ == "__main__":
    outfile, md_files = get_md_files()
    parse_tags(outfile, md_files)
