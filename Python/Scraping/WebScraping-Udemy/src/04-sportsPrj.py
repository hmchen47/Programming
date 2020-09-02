#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

"""
Scraping 2012 Premier League Data

1. Team name
2. Points

URL: https://www.skysports.com/premier-league-table/2011
"""

import requests


def download_pg(url):

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    page = requests.get(url, headers=headers)

    return page

def main(debug=False):

    url = "https://www.skysports.com/premier-league-table/2011"

    page = download_pg(url)

    print("\nmain web page status code: {}".format(page.status_code))

    # print("\nhtml source file in text; \n{}".format(page.text))

    input("\nPress enter to continue ...\n")

    soup = BeautifulSoup(page.text, 'html.parser')

    # print("\n\n\n---------------------------------------------\n")
    # print("soup after render by BeautifulSoup w/ html.parser: \n{}".format(soup.prettify))


    # input("\nPress enter to continue ...\n")

    # get all a tag elements and contents
    href_lst = soup.find_all('a')

    # print("\nDisplay all hyperlinks:")
    # for href in href_lst:
    #     print("\n{}".format(href))

    # input("\nPress enter to continue ...\n")

    # get the contents of a table w/ class
    league = soup.find('table', class_ = 'standing-table__table')

    print("\nDisplay all info w/ the table: \n{}".format(league))

    return None


if __name__ == "__main__":
    
    print("\nExample: Sports - Primier League 2011")

    main(debug=True)
    # main()

    print("\nEnd of Example: Sports - Primier League 2011")

