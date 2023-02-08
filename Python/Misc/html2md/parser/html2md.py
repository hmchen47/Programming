#!/home/hmchen/.venvs/html2md-Z6Rs3Moi/bin/python3

import argparse


def parse_args():
    """Parsing the command line args to read in files and target file path/name"""
    parser = argparse.ArgumentParser(
        description="Convert embedded HTML figures and tables code to markdown syntax"
    )
    parser.add_argument("inputs", nargs="*", help="Markdown files to process")


if __name__ == "__main__":
    mdfiles_lst = parse_args()
