#!/usr/bin/env python3

import os

from bs4 import BeautifulSoup


def replace_fig_tags(soup: BeautifulSoup, path: str) -> BeautifulSoup:
    """Replace figure tags w/ markdown figure syntax ~[alt text](link)

    Args:
        soup (str): BeautifulSoup text
    """
    # remove div and
    for fig_set in soup.find_all(
        "div", attrs={"style": "display: flex; justify-content: center;"}
    ):
        for img_tag in fig_set.find_all("img"):
            if "http" in img_tag["src"]:
                fig_set.insert_after(f"\n\n![{img_tag['src']}]({img_tag['alt']})")
            else:
                fig_set.insert_after(
                    f"\n\n![os.path.join(path, {img_tag['src']})]({img_tag['alt']})"
                )

        fig_set.extract()

    return soup.prettify()


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
    replace_fig_tags(soup, os.path.basename(fname))
    print("\n\n\n**********************************************\n\n")
    print(soup)
