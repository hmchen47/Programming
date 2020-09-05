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

def rmStr():
    return [re.compile(r"和_圖_書"), re.compile(r"和-圖-書"), re.compile(r"和圖書"), re.compile(r"和\*圖\*書"), \
        re.compile(r"https://m\.hetubook\.com\.com"), re.compile(r"ｍ•hetｕｂｏok\.cｏm\.ｃｏm"), \
        re.compile(r"m\.ｈeｔｕｂｏｏk•cｏｍ\.ｃoｍ"), re.compile(r"ｗｗw•heｔuｂｏｏk\.com\.ｃom"), \
        re.compile(r"ｈtｔps://wｗw•ｈeｔubook•com\.coｍ"), re.compile(r"hetubook\.com\.com"), \
        re.compile(r"www\.hｅｔubooｋ•com\.coｍ"), re.compile(r"m•ｈetubook\.cｏm\.com"), \
        re.compile(r"hｅｔubook\.cｏｍ\.cｏm"), re.compile("hｅtuｂoｏk•ｃｏｍ\.ｃｏｍ"), \
        re.compile("htｔｐs://ｍ•hｅtｕｂｏoｋ•com\.coｍ"), re.compile("hｔtｐs://ｍ\.ｈeｔｕboｏｋ•coｍ•ｃｏm"), \
        re.compile("m\.ｈeｔｕbｏｏｋ\.ｃｏm•cｏｍ"), re.compile(r"hｔｔps://www\.hetｕbｏｏｋ•cｏｍ•ｃｏm"), \
        re.compile(r"ｈｔtps://ｍ\.ｈetuｂoｏk•ｃom\.ｃom"),  re.compile(r"https://ｗww•ｈetｕbｏｏk•ｃom•ｃom"), \
        re.compile(r"hｔtｐs://m\.ｈeｔuｂｏoｋ•ｃｏｍ•ｃom"), re.compile(r"ｗｗw•hetｕｂook•ｃｏm\.ｃom"), \
        re.compile(r"hｅtuｂｏｏk•cｏm\.ｃoｍ"), re.compile("ｈeｔuｂｏｏｋ•ｃｏｍ\.ｃoｍ"), \
        re.compile(r"wwｗ•hｅtuｂｏoｋ•ｃｏｍ•ｃｏｍ"), re.compile(r"hｔｔps://ｍ•hetｕbｏok.ｃoｍ•cｏm"), \
        re.compile(r"ｍ•ｈetｕｂook•cｏｍ•cｏm"), re.compile(r"hｔｔｐs://ｗww\.ｈｅｔuｂoｏk•ｃｏm\.cｏm"), \
        re.compile(r"ｈｔtps://m•heｔuｂook•cｏm•cｏm"), re.compile(r"htｔｐs://ｗww\.heｔｕbｏok\.ｃｏｍ•ｃom"), \
        re.compile(r"ｍ\.ｈetｕbｏok•cｏm\.cｏm"), re.compile(r"ｈｔｔps://ｗｗｗ\.hｅｔｕbooｋ\.cｏｍ•ｃom"), \
        re.compile(r"m•hｅｔｕｂoｏk•ｃoｍ•cｏｍ"), re.compile(r"hｔｔps://ｍ•heｔubooｋ•com\.coｍ"), \
        re.compile(r"ｈｔtｐs://ｗww•ｈeｔｕbｏｏｋ•ｃoｍ•com"), re.compile(r"www•hetuｂｏok•ｃom•coｍ"), \
        re.compile(r"ｈｅｔuｂoｏｋ\.ｃｏm\.cｏｍ"), re.compile(r"ｈetｕｂook\.cｏm\.cｏm"), \
        re.compile(r"ｈｔtps://ｗww\.heｔuｂｏｏｋ•ｃｏm\.cｏm"), re.compile(r"hｔｔｐs://wｗｗ•ｈeｔuｂooｋ\.com\.ｃom"), \
        re.compile(r"ｗww\.hｅｔｕｂｏｏｋ\.cｏm•ｃom"), re.compile(r"wｗw\.ｈｅｔｕbｏｏk\.com•ｃom"), \
        re.compile(r"https://ｗｗｗ•hｅtuｂook\.ｃom\.ｃｏｍ"), re.compile(r"ｈetuｂoｏｋ•coｍ•com"), \
        re.compile(r"www•ｈeｔuboｏｋ•com•cｏｍ"), re.compile(r"ｈｔtps://ｗｗw•ｈeｔuｂooｋ\.ｃｏｍ\.coｍ"), \
        re.compile(r"ｈｅtubｏｏｋ•coｍ•ｃｏｍ"), re.compile(r"wｗw•hｅｔｕbｏｏk•ｃｏm•ｃｏm"), \
        re.compile(r"ｈtｔｐs://m\.hｅtｕｂoｏk•ｃom\.ｃom"), re.compile("ｈtｔps://ｗｗｗ\.ｈｅｔｕｂooｋ•cｏｍ\.coｍ"), \
        re.compile(r"ｈtｔps://heｔｕbｏok•com\.ｃｏm"), re.compile(r"ｍ•ｈeｔｕｂｏｏｋ\.com\.ｃoｍ"), \
        re.compile(r"m•hｅtｕｂook•ｃｏm\.ｃｏｍ"), re.compile(r"ｈｔｔｐs://ｍ\.hｅtｕｂoｏｋ\.ｃｏｍ•coｍ"), \
        re.compile(r"ｈｔtps://ｍ\.hｅtｕｂｏｏk•cｏｍ•ｃｏｍ"), re.compile(r"ｗww•ｈｅtuboｏｋ•ｃｏm•coｍ"), \
        re.compile("ｈｔtｐs://ｗwｗ•hｅｔｕbｏｏｋ\.cｏm•ｃｏm"), re.compile(r"ｈtｔｐs://ｗww•ｈetｕｂｏｏk•ｃｏｍ•cｏｍ"), \
        re.compile(r"ｗｗｗ•hｅｔuｂook\.cｏm•ｃｏｍ"), re.compile("ｈetｕｂｏoｋ\.ｃｏｍ\.ｃｏｍ"), \
        re.compile(r"httｐs://ｗｗw•hｅtｕbooｋ\.coｍ\.com"), re.compile(r"ｗｗw•ｈeｔｕbｏｏk\.ｃoｍ\.ｃｏｍ"), \
        re.compile(r"heｔuｂoｏｋ\.cｏｍ•coｍ"), re.compile(r"htｔｐs://wｗｗ\.ｈｅｔｕｂoｏｋ•com\.ｃom"), \
        re.compile(r"m•hetuｂooｋ•ｃｏｍ\.ｃoｍ"), re.compile("httｐs://ｍ•ｈetubooｋ•cｏｍ\.cｏm"), \
        re.compile(r"hｔtｐs://ｍ•ｈetuｂoｏk•cｏm•cｏm"), re.compile(r"ｈｔｔｐs://m•ｈｅｔｕｂooｋ•ｃoｍ\.ｃｏm"), \
        re.compile(r"hｔtps://ｍ•ｈｅｔｕｂook\.ｃｏｍ\.ｃｏm"), re.compile(r"ｗｗw•ｈeｔuｂｏoｋ\.cｏm•ｃom"), \
        re.compile(r"hｔｔps://m\.ｈetuｂｏｏk\.ｃoｍ\.ｃｏｍ"), re.compile(r"hｅｔubｏok\.ｃoｍ\.cｏm"), \
        re.compile(r"ｍ•ｈeｔｕbｏok•cｏｍ\.ｃom"), re.compile(r"ｍ\.ｈetuｂoｏｋ\.ｃoｍ•ｃom"), \
        re.compile(r"ｗww\.ｈｅtuｂoｏk\.coｍ\.ｃｏm"), re.compile(r"m\.hetｕｂｏoｋ•ｃom•ｃｏｍ"), \
        re.compile(r"wｗw•heｔubｏｏｋ•com\.cｏｍ"), re.compile(r"ｈtｔｐs://m\.heｔuｂｏｏk\.cｏm•com"), \
        re.compile("m\.heｔuｂoｏk•coｍ•ｃｏｍ"), re.compile(r"ｍ•hｅtｕｂoｏk•cｏｍ•ｃｏｍ"), \
        re.compile(r"ｈeｔｕｂoｏｋ\.com\.ｃｏm"), re.compile(r"hｔｔps://ｗｗｗ•ｈetuｂｏｏk•ｃoｍ\.ｃoｍ"), \
        re.compile(r"heｔｕboｏk•ｃｏｍ•cｏｍ"), re.compile(r"hｔｔps://heｔubｏoｋ\.cｏm•ｃｏm"), \
        re.compile(r"ｈeｔｕbｏｏk•ｃom•ｃom"), re.compile(r"ｗｗｗ•ｈｅtｕｂoｏｋ•coｍ•cｏｍ"), \
        re.compile(r"hetubｏｏｋ•cｏｍ•coｍ"), re.compile(r"ｈｔtｐs://ｍ•hｅｔuｂｏｏｋ•cｏｍ•cｏｍ"), \
        re.compile(r"ｈｅtubｏoｋ\.com•coｍ"), re.compile(r"ｈｔｔps://wｗｗ•ｈeｔｕｂoｏk\.ｃoｍ•cｏm"), \
        re.compile(r"ｍ•hｅｔｕbooｋ•cｏm\.cｏｍ"), re.compile(r"httｐs://ｗｗw\.ｈｅｔuｂｏok\.ｃｏm\.ｃｏｍ"), \
        re.compile(r"hｔtｐs://m•ｈｅtuboｏｋ•ｃom\.ｃoｍ"), re.compile(r"ｈttｐs://wｗw\.hetubｏｏk•ｃoｍ\.ｃｏm"), \
        re.compile(r"m\.heｔｕｂook•ｃoｍ\.ｃｏm"), re.compile(r"m\.hetubｏoｋ•cｏm\.coｍ"), \
        re.compile(r"ｈｔｔps://ｗｗｗ\.ｈetuｂｏoｋ\.ｃｏｍ•cｏm"), re.compile(r"ｈtｔps://wｗw•ｈｅtｕbooｋ\.ｃｏm•cｏm"), \
        re.compile(r"ｗwｗ\.hetｕｂoｏk\.ｃｏｍ•com"), re.compile(r"hetｕｂoｏk\.ｃom\.ｃoｍ"), \
        re.compile(r"hｅtｕbｏok•ｃom•cｏｍ"), re.compile(r"m•hｅtｕbooｋ•com\.ｃｏm"), \
        re.compile(r"ｈetｕbｏoｋ•ｃoｍ\.ｃｏｍ"), re.compile(r"ｍ\.ｈeｔｕbｏｏk\.ｃom•cｏｍ"), \
        re.compile(r"ｍ•ｈeｔｕｂooｋ\.com•cｏｍ"), re.compile(r"ｍ\.hetubook\.ｃｏm•ｃｏm"), \
        re.compile(r"ｈｔｔps://ｗww•hetuｂｏｏｋ\.cｏm•com"), re.compile(r"ｈｔtps://ｍ\.hｅtubｏoｋ\.cｏｍ•ｃoｍ"), \
        re.compile(r"m•ｈeｔuｂｏoｋ•ｃoｍ.com"), e.compile(r"m•heｔuｂｏok•ｃｏm\.ｃｏｍ"), \
        re.compile(r"ｍ•ｈｅｔuｂｏoｋ\.ｃｏｍ\.com"), re.compile(r"wwｗ\.ｈeｔｕbooｋ•cｏm•cｏm"), \
        re.compile(r"ｈtｔｐs://wｗｗ•hｅｔuｂooｋ\.ｃｏｍ\.cｏｍ"), re,compile(r"ｍ.hｅｔubｏok•cｏm.ｃｏｍ"), \
        re.compile(r"ｈetuｂｏｏｋ•coｍ•ｃom"), re.compile(r"https://www\."), re.compile(r"www\.") \
        ]


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
        
        # ch_content = re.sub(substr, '', ch_content)
        # append_chapter_content(chapter[0], )

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
        time.sleep(1)


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



