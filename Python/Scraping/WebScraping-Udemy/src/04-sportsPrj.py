#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import pandas as pd
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

    # print("\nDisplay all info w/ the table: \n{}".format(league_tbl))

    # input("\nPress enter to continue ...\n")

    # extract team name and points from the table
    league_tbl = league.find_all('tbody')
    teams_info = []
    for league_teams in league_tbl:
        rows = league_teams.find_all('tr')
        for row in rows:
            team_name = row.find('td', class_='standing-table__cell standing-table__cell--name').text.strip()
            team_pts = row.find_all('td', class_='standing-table__cell')[9].text.strip()
            teams_info.append({'name': team_name, 'points': int(team_pts)})
    
    print("Display all team names and their points in 2011-2012:")
    for team_info in teams_info:
        print("  {:26s} w/ {:3d} points".format(team_info['name'], team_info['points']))

    input("\nPress enter to continue ...\n")

    # write the info into a dataframe
    league2011_df = pd.DataFrame(teams_info)

    print(league2011_df.head())

    return None


if __name__ == "__main__":
    
    print("\nExample: Sports - Primier League 2011")

    main(debug=True)
    # main()

    print("\nEnd of Example: Sports - Primier League 2011\n")

