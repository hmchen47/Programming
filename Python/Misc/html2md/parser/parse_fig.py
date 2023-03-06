#!/home/hmchen/.venvs/html2md-Z6Rs3Moi/bin/python3

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
        fig_set.insert_after(f"2 Figures\n")
        for img_tag in fig_set.find_all("img"):
            if "http" in img_tag["src"]:
                fig_set.insert_after(f"![{img_tag['alt']}]({img_tag['src']})\n")
            else:
                fig_set.insert_after(
                    f"![{img_tag['alt']}]({os.path.join(path, img_tag['src'])})\n"
                )

        fig_set.extract()

    # remove figure elements
    for fig_tag in soup.find_all("figure"):
        fig_tag.insert_after(f"Figure\n")
        for img_tag in fig_tag.find_all("img"):
            if "http" in img_tag["src"]:
                fig_tag.insert_after(f"![{img_tag['alt']}]({img_tag['src']})\n")
            else:
                fig_tag.insert_after(
                    f"![{img_tag['alt']}]({os.path.join(path, img_tag['src'])})\n"
                )
            fig_tag.extract()

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
    soup = replace_fig_tags(soup, os.path.basename(fname))
    print("\n\n\n**********************************************\n\n")
    print(soup)
