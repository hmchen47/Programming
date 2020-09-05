#!/usr/bin/env python3
# -*- coding-utf-8 -*-

import requests
import re
import time
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

def syntax_chk(txt, debug=False):
    """syntax check w/ a predefined database in db/syntax.csv

    Args:
        txt (str): the string to check its syntax
        debug (bool, optional): turn on/off debug message. Defaults to False.
    """

    # CODE to be filled

    return txt


def write_book_info(fname, info, debug=False):
    """create stored file with given book title, author and introduction

    Args:
        fname (str): file name for stored file
        info (lst): a list of text w/ book title, author, and book intro
        debug (bool, optional): turn on/off debug message. Defaults to False.
    """
    # create/overwrite store file
    with open(fname, "w", encoding='utf-8') as fd:
        fd.write("《{}》\n\n".format(info[0]))
        fd.write("{}\n\n\n\n".format(info[1]))

        intro_txt = syntax_chk(''.join(info[2]))

        fd.write("本書簡介：\n\n{}\n\n\n\n".format(intro_txt))

    fd.close
    
    return None


def reRmStr(s, e):

    re_rm_str = r"[\whttps://m\.ww\.ｈｔtps://ｈｔtｐs／•:ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ１２３４５６７８９０\+]*"

    return re.compile(s+re_rm_str+e)


def append_chapter_content(fname, title, contents):

    # wite content into file
    with open(fname, "a+", encoding='utf-8') as fd:
        fd.write("正文 {}\n\n\n".format(title))
        fd.write("{}\n\n\n\n\n\n\n".format(contents))

    fd.close
    
    return None

def scrape_chapter(chapter, fname, purl, debug=False):
    """scrape chapter and its contents

    Args:
        chapter (tuple): a tuple contains (chapter title, chapter link)
        fname (str): file name to store chapter contes
        purl (str): the url link to the website of hetubook.com
        debug (bool, optional): turn on/off debuging message. Defaults to False.
    """

    # open chapter url
    ch_pg = requests.get(purl+chapter[1], headers=headers)

    if ch_pg.status_code != 200:
        print("\nreturn chapter page {} w/ status code: {}".format(chapter[0], main_pg.status_code))
        exit(True);

    soup = BeautifulSoup(ch_pg.text, "html.parser")

    contents = soup.find('div', id='content').find_all('div')

    ch_paragraphs = []
    for paragraph in contents:
        ch_paragraphs.append(paragraph.text.strip())

    ch_content = '\n\n'.join(ch_paragraphs)

    rm_substrs = [re.compile(r"和_圖_書"), re.compile(r"和-圖-書"), re.compile(r"和圖書"), re.compile(r"和\*圖\*書")]
    for start in [r"h", r"m", r"w", r"ｈ", r"ｍ", r"ｗ"]:
        for end in [r"m", r"ｍ", r"ｏ"]:
            rm_substrs.append(reRmStr(start, end))

    # if debug:
        # print("\nRemoved substring w/ regex: \n{}\n".format('\n\n'.join(rm_substrs)))

    for substr in rm_substrs:
        if debug and len(re.findall(substr, ch_content)) >0:
            print("\nw/ {}: \n{}".format(substr, re.findall(substr, ch_content)))
        
        ch_content = re.sub(substr, '', ch_content)
    
    append_chapter_content(fname, chapter[0], ch_content)

    if debug:
        print("\nChapter contents: \n{}".format(ch_content))

    return None



def parse_chapters(main_soup, purl, fname, debug=False):
    """extract chapter names and links from main page , then pass to
    scrape the contents of the chapter and write into file

    Args:
        main_soup (html obj): HTML BeautifulSoup object of main page
        purl (str): url of web site
        fname (str): filename of the file to store contents
        debug (bool, optional): turn on/off debug message. Defaults to False.
    """

    chapters = []

    # extract chapter titles and their links to 
    directory = main_soup.find('dl', id='dir').find_all('dd')

    for chapter in directory:
        link = chapter.find('a')
        chapters.append((link.get('title'), link.get('href')))

    # if debug:
    #     print("Chapter directory: \n{}\n\n".format(chapters))

    # scrape chapter and extract contents
    cnt = 0
    for chapter in chapters:
        scrape_chapter(chapter, fname, purl)
        time.sleep(0.3)
        cnt += 1
        if cnt%50 == 0:
            print("Scraping done on: {}".format(chapter[0]))

    return None


def main(purl, burl, headers, debug=False):

    main_pg = requests.get(purl+burl, headers=headers)
    if main_pg.status_code != 200:
        print("\nreturn main web page status code: {}".format(main_pg.status_code))
        exit(True);

    soup = BeautifulSoup(main_pg.text, "html.parser")

    title, author, intro = parse_book_info(soup)

    # format book filename
    fname = "./novel/{}.[{}].txt".format(author.strip('作者：').strip(), title)
    
    write_book_info(fname, [title, author, intro])
    
    parse_chapters(soup, purl, fname, debug)

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



