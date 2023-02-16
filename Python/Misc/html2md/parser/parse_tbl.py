#!/usr/bin/env python3

import os

import htmltabletomd
from bs4 import BeautifulSoup


def replace_tbl_tags(soup: BeautifulSoup) -> BeautifulSoup:
    """Replace figure tags w/ markdown figure syntax ~[alt text](link)

    Args:
        soup (class): BeautifulSoup text
    """
    for tbl_tag in soup.find_all(
        "table",
        attrs={
            "align": "center",
            "border": "1",
            "cellpadding": "5",
            "cellspacing": "0",
        },
    ):
        md_tbl = htmltabletomd.convert_table(str(tbl_tag))

        # find all tags in table
        tbl_soup = BeautifulSoup(md_tbl, "html.parser")
        tags = {tag.name for tag in tbl_soup if tag.name != None}

        print(f"\n------------------------------------\n\n{tbl_soup}\n")
        # replace tags w/ associated md or latex code
        for tag in tags:
            for cell_tag in tbl_soup.find_all(tag):
                if tag == "br":
                    cell_tag.insert_after("$\\\\$")
                    cell_tag.unwrap()
                elif tag == "sup":
                    cell_tag.insert_after(f"$^{{{cell_tag.string}}}$")
                    cell_tag.decompose()
                elif tag == "sub":
                    cell_tag.insert_after(f"$_{{{cell_tag.string}}}$")
                    cell_tag.decompose()
                elif tag == "code":
                    cell_tag.insert_after(f"`{cell_tag.string}`")
                    cell_tag.decompose()
                elif tag == "i" or tag == "em":
                    cell_tag.insert_after(f"*{cell_tag.string}*")
                    cell_tag.decompose()
                elif tag == "b" or tag == "strong":
                    cell_tag.insert_after(f"**{cell_tag.string}**")
                    cell_tag.decompose()
                elif cell_tag == 'a':
                    # the local link not processed, it should be processed in the original html code
                    cell_tag.insert_after(f'[{cell_tag.string}]{{cell_tag['src']}}')
                    cell_tag.decompose()
                else:
                    print(f"Not processed tag {cell_tag}, add case to handle it!")
        print(f"\n************************************\n\n{tbl_soup}\n")

    return soup.prettify()


if __name__ == "__main__":
    fname = "/home/hmchen/Projects/Programming/Notes/gc01-FloatPt.md"
    with open(fname, "r", encoding="utf-8") as in_fd:
        content = in_fd.read()

    soup = BeautifulSoup(content, "html.parser")
    print("\n\n")
    # print(type(soup))
    print("\n\n=========================================")
    replace_tbl_tags(soup)
    print("\n\n\n**********************************************\n\n")
    # print(soup)
