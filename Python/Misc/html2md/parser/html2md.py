#!/home/hmchen/.venvs/html2md-Z6Rs3Moi/bin/python3

import argparse
import errno
import os
import stat
import sys
import time

import mdformat
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
        output_md = os.path.join(
            os.path.join(os.path.join(base_dir, DEFAULTDIR), args.output)
        )
    else:
        output_md = os.path.join(
            os.path.join(base_dir, os.path.join(DEFAULTDIR, DEFAULTOUT))
        )

    # remove output markdown file if exist
    try:
        os.chmod(output_md, stat.S_IWUSR)
        os.remove(output_md)
    except OSError as err:
        if err.errno != errno.ENOENT:  # no such file or directory
            raise  # re-raise exception if a different error occurred

    return (output_md, input_files)


def remove_tags(soup: BeautifulSoup) -> str:
    """remove remaining tags in markdown file

    Args:
        soup (BeautifulSoup): markdown file as BeautifulSoup object

    Returns:
        str: markdown file in string text
    """
    tags = {tag.name for tag in soup if tag.name != None}

    for tag in tags:
        for doc_tags in soup.find_all("tag"):
            if tag == "br":
                cell_tag.insert_after("$\\\\$")
                cell_tag.unwrap()
            elif tag == "i" or tag == "em":
                cell_tag.insert_after(f"*{cell_tag.string}*")
                cell_tag.decompose()
            elif tag == "b" or tag == "strong":
                cell_tag.insert_after(f"**{cell_tag.string}**")
                cell_tag.decompose()
            else:
                print("{tag} not processed, proccessing required?")

    return mdformat.text(str(soup))


def write_outfile(output_md_file: str, md_output: str):
    """write mardown output to file

    Args:
        output_md_file (str): output filename
        md_output (str): contents to write to output file
    """
    with open(output_md_file, "a+", encoding="utf-8") as df_out:
        df_out.write(md_output)
        df_out.write(f"\n" * 6)

    time.sleep(0.5)
    os.chmod(output_md_file, stat.S_IWUSR)

    return None


def parse_tags(output_md_file: list, md_files: list) -> str:
    """parsing embedded html tags to relative markdown syntax

    Args:
        output_md_file (lst): output filename
        md_files (lst): [md_file1, md_file2, ...]

    Returns:
        fd: file descriptor of output filename
    """
    print()
    for md_file in md_files:
        with open(md_file, "r", encoding="utf-8") as md_fd:
            soup = BeautifulSoup(md_fd.read(), "html.parser")
            soup = replace_fig_tags(soup, os.path.dirname(md_file))
            soup = replace_tbl_tags(soup)
            md_output = remove_tags(soup)

            print(f"\nComplete parsing tags in {md_file}!!")
            write_outfile(output_md_file, md_output)

    return output_md_file


if __name__ == "__main__":
    outfile, md_files = get_md_files()
    print(
        f"\nConvert files {[os.path.basename(file) for file in md_files]}\n\nin dir {os.path.dirname(md_files[0])} to markdown file \n\t{outfile}"
    )
    parse_tags(outfile, md_files)
