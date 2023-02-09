#!/usr/bin/env python3

import errno
import os
import time

import html2md
import parse_fig
from bs4 import BeautifulSoup


def rm_silent(fname):
    """remove a file

    Args:
        fname (str): the file to remove w/ full path filename
    """
    try:
        os.remove(fname)
    except OSError as err:
        if err.errno != errno.ENOENT:  # no such file or directory
            raise  # re-raise exception iif a differnet error occurred


def read_and_write_md(out_file, in_files):
    """read all given md files and write into a single output md file

    Args:
        out_file (str): output markdown file w/ path
        in_files (str list): a list of input markdown files w/ or w/o embedded html figure and table html code
    """
    rm_silent(out_file)

    for fname in in_files:
        with open(fname, mode="r", encoding="utf-8") as in_fd:
            content = in_fd.read()
            soup = BeautifulSoup(content, "html.parser")
            print(soup)
            print("\n\n\n-------------------------------------------\n\n\n")
            soup = substitute_fig_tags(soup)
            time.sleep(2)


if __name__ == "__main__":
    outfile, md_files = html2md.get_md_files()
    read_and_write_md(outfile, md_files)
