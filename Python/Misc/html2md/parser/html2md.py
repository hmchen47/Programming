#!/home/hmchen/.venvs/html2md-Z6Rs3Moi/bin/python3

import argparse


def get_mdfiles():
    """Parsing the command line args to read in files and target file path/name"""
    parser = argparse.ArgumentParser(
        description="Convert embedded HTML figures and tables code to markdown syntax"
    )
    parser.add_argument(
        "inputs", nargs="*", default="reading_in.md", help="Markdown files to process"
    )
    parser.add_argument(
        "-d",
        "--dir",
        default="../working",
        help="The folder to retrieve markdown files",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="./working/reading.md",
        help="Output markdown file for pandoc to process",
    )

    args = parser.parse_args()

    # generate list of read in markdown files
    infiles = []
    for fname in args.inputs:
        print(args.dir)
        print(fname)
        # infiles.append(join(args.dir, fname))

    return (args.output, infiles)


if __name__ == "__main__":

    outfile, mdfiles = get_mdfiles()
    print(mdfiles)
    print(outfile)
