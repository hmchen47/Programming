#!/usr/bin/env python3
# -*- coding-utf-8 -*-

import sys
import scrapy

# from datetime import datetime
# from scrapy.http import Request, FormRequest, TextResponse
# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor
# from scrapy.spider import Spider
# from scrapy.selector import Selector
# from scrapy import log
# from ..items import HosItem

import requests
import re
from bs4 import BeautifulSoup


def parse_book_title(soup, debug=False):
    """parsing book title from main page

    Args:
        soup (str): html contents of main web page
        debug (boolean): turn on/off debug msg, default=False
    """
    txt = re.compile(r"book_info finish[\w]*<h2>(.+?)</h2>")
    if debug:
        print("Parse Book title: {}".format(txt))

    try:
        title = re.search(txt, soup).group(1)
    except AttributeError as err:
        print("Book title extract error: {}".format(err))
        exit(True)

    return title.group(1)


def main(purl, burl, headers, debug=False):

    main_page = requests.get(purl+burl, headers=headers)
    if main_page.status_code != 200:
        print("\nreturn main web page status code: {}".format(main_page_status))
        exit(True);

    if debug:
        print("\nmain page encoding: {}".format(main_page.encoding))

    soup = BeautifulSoup(main_page.content, "html.parser")
    if debug:
        print(soup)

    title = parse_book_title(soup, debug)
    # author = get_book_author(soup, debug)

    # intro_txt = get_intro(soup, debug)

    # chp_lst = list_chapter(soup)

    # p_name = "./novel/{}.[{}].txt".format(author, title)

    # f_hdl = open(p_name, "w+")


    return None


if __name__ == "__main__":
    
    purl = "https://www.hetubook.com"
    burl = "/book/2600/index.html"
    # header = {Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) CChrome/70.0.3538.77 Safari/537.36'}
    auth = ('user', 'pass')
    payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
    # requests.get('https://httpbin.org/get', params=payload)

    debug = True
    f_hdl = main(purl, burl, headers, debug)



