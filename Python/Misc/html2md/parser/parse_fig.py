#!/usr/bin/env python3

import os

from bs4 import BeautifulSoup


def replace_fig_tags(soup: BeautifulSoup, path: str) -> BeautifulSoup:
    """Replace figure tags w/ markdown figure syntax ~[alt text](link)

    Args:
        soup (str): BeautifulSoup text
    """
    # remove div and figure elements
    for fig_set in soup.find_all(
        "div", attrs={"style": "display: flex; justify-content: center;"}
    ):
        for img_tag in fig_set.find_all("img"):
            if "http" in img_tag["src"]:
                fig_set.insert_after(f"![{img_tag['src']}]({img_tag['alt']})")
            else:
                fig_set.insert_after(
                    f"![os.path.join(path, {img_tag['src']})]({img_tag['alt']})"
                )

        fig_set.clean()

    # remove figure elements
    for fig_tag in soup.find_all(
        "figure",
        attrs={
            "style": "display: flex; margin: 0.5em; justify-content: center; align-items: center;"
        },
    ):
        if img_tag in fig_tag.find_all("img"):
            fig_tag.insert_after(f"![{img_tag['src']}]({img_tag['alt']})")
        else:
            fig_tag.insert_after(
                f"![os.path.join(path, {img_tag['src']})]({img_tag['alt']})"
            )
        fig_tag.clean()

    return soup


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
