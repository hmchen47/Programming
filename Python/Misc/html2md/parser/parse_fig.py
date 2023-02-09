#!/usr/bin/env python3

from bs4 import BeautifulSoup


def substitute_fig_tags(soup):
    """Replace figure tags w/ markdown figure syntax ~[alt text](link)

    Args:
        soup (str): BeautifulSoup text
    """
    pass


if __name__ == "__main__":
    with open(
        "~/Projects/Programming/Notes/web09-CSSLayout.md", "r", encoding="utf-8"
    ) as in_fd:
        content = in_fd.read()

    soup = BeautifulSoup(content, "html.parser")
    substitute_fig_tags(soup)
