#!/usr/bin/env python3

from bs4 import BeautifulSoup


def append_md_figs(soup: BeautifulSoup, srcs: str, alts: str) -> BeautifulSoup:
    pass


def replace_fig_tags(soup: BeautifulSoup) -> BeautifulSoup:
    """Replace figure tags w/ markdown figure syntax ~[alt text](link)

    Args:
        soup (str): BeautifulSoup text
    """
    # remove div and
    for fig_set in soup.find_all(
        "div", attrs={"style": "display: flex; justify-content: center;"}
    ):
        srcs = []
        alts = []
        for img_tag in fig_set.find_all("img"):
            srcs.append(img_tag["src"])
            alts.append(img_tag["alt"])

        append_md_figs(soup, srcs, alts)


if __name__ == "__main__":
    with open(
        "/home/hmchen/Projects/Programming/Notes/gc01-FloatPt.md",
        "r",
        encoding="utf-8",
    ) as in_fd:
        content = in_fd.read()

    soup = BeautifulSoup(content, "html.parser")
    print("\n\n\n")
    print(type(soup))
    print("\n\n=========================================")
    replace_fig_tags(soup)
    print("\n\n\n**********************************************\n\n")
    # print(soup)
