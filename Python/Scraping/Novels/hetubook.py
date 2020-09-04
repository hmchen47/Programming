#!/usr/bin/env python3
# -*- coding-utf-8 -*-

import requests
import re
from bs4 import BeautifulSoup

def parse_book_info(main_pg, debug=False):
    """parsing book title from main page

    Args:
        main_pg (request.Response): html contents of main web page
        debug (boolean): turn on/off debug msg, default=False
    """
    title_sec = main_pg.find('div', class_="book_info finish")
    
    title = title_sec.find('h2').get_text()
    author = title_sec.find('div').get_text()

    intro = []
    intro_div = title_sec.find('div', class_='intro')
    intro_paras = intro_div.find_all('p')
    for para in intro_paras:
        intro.append(para.get_text()+'\n\n')

    if debug:
        print("Book title: {}".format(title))
        print("Author: {}".format(author))
        print("Book intro: \n{}".format(intro))


    return title, author, intro


def main(purl, burl, headers, debug=False):

    main_pg = requests.get(purl+burl, headers=headers)
    if main_pg.status_code != 200:
        print("\nreturn main web page status code: {}".format(main_pg.status_code))
        exit(True);

    if debug:
        print("\nmain page encoding: {}".format(main_pg.encoding))

    soup = BeautifulSoup(main_pg.text, "html.parser")

    title, author, intro = parse_book_info(soup, debug)
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



