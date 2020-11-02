#!/usr/bin/env python3
# -*-coding: utf-8 -*-


from lxml import html
import requests

import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from bs4 import BeautifulSoup

pd.options.display.max_columns=50

def print_element(element):
    print("<{:s} {:s}>: {:s} ...".format(element.tag, element.attrib, \
        element.text_content()[:200].replace("\n", " ")))


def main():

    page = requests.get("https://en.wikipedia.org/wiki/List_of_Nobel_laureates")
    tree = BeautifulSoup(page.text, 'lxml')
    print(tree)
    # print_element(tree)


    return None

if __name__ == "__main__":

    print("\nWeb scraping for Nobel laureates from Wikipedia ...\n")

    main()

    print("\nEnd of Web scraping for Nobel laureates from Wikipedia ...\n")

