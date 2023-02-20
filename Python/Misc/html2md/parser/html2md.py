#!/home/hmchen/.venvs/html2md-Z6Rs3Moi/bin/python3

import argparse
import errno
import os
import stat
import sys
import time

from bs4 import BeautifulSoup

# add the Python path at runtime
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(1, os.path.join(base_dir, "parser"))

from parse_fig import replace_fig_tags
from parse_tbl import replace_tbl_tags

DEFAULTDIR = "working"
DEFAULTOUT = "notes_reading.md"


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


def write_outfile(outfile: str, md_output: str):
    """write mardown output to file

    Args:
        outfile (str): output filename
        md_output (str): contents to write to output file
    """
    try:
        os.chmod(outfile, stat.S_IWUSR)
        os.remove(outfile)
    except OSError as err:
        if err.errno != errno.ENOENT:  # no such file or directory
            raise  # re-raise exception if a different error occurred

    with open(outfile, "a+", encoding="utf-8") as df_out:
        df_out.write(md_output)

    time.sleep(0.5)
    os.chmod(outfile, stat.S_IWUSR)

    return None


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
            soup = replace_fig_tags(soup, os.path.dirname(md_file))
            md_output = replace_tbl_tags(soup)

            print(f"Complete parsing tags in {md_file}!!\n")
            write_outfile(outfile, md_output)

    return outfile


if __name__ == "__main__":
    outfile, md_files = get_md_files()
    print(
        f"\nConvert files {[os.path.basename(file) for file in md_files]}\n\nin dir {os.path.dirname(md_files[0])} to markdown file \n\t{outfile}"
    )
    parse_tags(outfile, md_files)
