#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import pandas as pd
from bs4 import BeautifulSoup


# Project: Movie Dataset
#
# get Wikipedia Dataset: List of Game of Thrones episodes 

# URL: https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes


def main(debug=False):

    url = "https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes"

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    pg = requests.get(url, headers=headers)

    if debug:
        print("Main page retriveing status: {}".format(pg.status_code))

    soup = BeautifulSoup(pg.text, 'html.parser')

    # if debug:
    #     print("\nsoup info: \n{}".format(list(filter(lambda x: (x != ''),\
    #         [soup.text.split('\n')[idx] for idx in range(6)]))))

    # get the desired table

    episodes_tbls = soup.find_all('table', class_='wikitable plainrowheaders wikiepisodetable')

    if debug:
        print("\nnumber of matched tables: {}".format(len(episodes_tbls)))

    episodes_lst = []
    for tbl in episodes_tbls:
        rows = tbl.find_all('tr', class_='vevent')
        for row in rows:
            # if debug:
            #     print(row.find_all('td'))
            
            season_no = row.find_all('td')[0].get_text()
            director = row.find_all('td')[2].get_text()
            episode_info = {'season No.': season_no, 'Director': director}
            episodes_lst.append(episode_info)

    episodes_df = pd.DataFrame(episodes_lst)

    print(episodes_df.head(15))

    return None



if __name__ == "__main__":

    print("\nExample: Movie Project......\n")

    main(debug=True)
    # main()

    print("\nEnf of Example: Movie Project......\n")
