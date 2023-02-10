#!/usr/bin/env python3

from bs4 import BeautifulSoup


def substitute_fig_tags(soup: BeautifulSoup) -> BeautifulSoup:
    """Replace figure tags w/ markdown figure syntax ~[alt text](link)

    Args:
        soup (str): BeautifulSoup text
    """
    pass


if __name__ == "__main__":
    with open(
        "/home/hmchen/Projects/Programming/Notes/web06-MVCOverview.md",
        "r",
        encoding="utf-8",
    ) as in_fd:
        content = in_fd.read()

    soup = BeautifulSoup(content, "html.parser")
    print(type(soup))
    print("\n\n\n=========================================\n\n\n")
    substitute_fig_tags(soup)
    print(soup)
