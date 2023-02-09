#!/usr/bin/env python3

import html2md
import os, errno, time


def read_and_write_md(out_file, in_files):
    """read all given md files and write into a single output md file

    Args:
        out_file (str): output markdown file w/ path
        in_files (str list): a list of input markdown files w/ or w/o embedded html figure and table html code
    """
    rm_silent(out_file)
    
    for file in in_files:
        with open(file, 'r') as fd:
            print(fd.read())
            print("\n\n\n")
            time.sleep(2)



if __name__ = "-__main__":
    outfile, md_files = get_md_files()
    read_and_write_md(outfile, md_files)
    
