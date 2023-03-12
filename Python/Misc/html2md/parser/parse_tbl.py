#!/use/bin/env python3

import os

from bs4 import BeautifulSoup


def replace_tbl_tags(soup: BeautifulSoup, path: str) -> BeautifulSoup:
    """Replace figure tags w/ markdown figure syntax ~[alt text](link)

    Args:
        soup (str): BeautifulSoup text
    """
    pass

    # return soup.prettify()


if __name__ == "__main__":
    fname = "/home/hmchen/Projects/Programming/Notes/gc01-FloatPt.md"
    with open(
        fname,
        "r",
        encoding="utf-8",
    ) as in_fd:
        content = in_fd.read()

    soup = BeautifulSoup(content, "html.parser")
    print("\n\n\n")
    print(type(soup))
    print("\n\n=========================================")
    replace_tbl_tags(soup, os.path.basename(fname))
    print("\n\n\n**********************************************\n\n")
    print(soup)
