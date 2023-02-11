#!/usr/bin/env python3

from bs4 import BeautifulSoup


def replace_fig_tags(soup: BeautifulSoup) -> BeautifulSoup:
    """Replace figure tags w/ markdown figure syntax ~[alt text](link)

    Args:
        soup (str): BeautifulSoup text
    """
    # remove div and
    for fig_set in soup.find_all(
        "div", attrs={"style": "display: flex; justify-content: center;"}
    ):
        for img_tag in fig_set.find_all("img"):
            fig_set.insert_after(f"\n\n![{img_tag['src']}]({img_tag['alt']})")

    fig_set.clear()

    return soup


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
    print(soup)
