#!/usr/bin/env python3

import sys

import aocd.get
import bs4
import requests

URL = "https://adventofcode.com/{year}/stats"


def _soup(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    return soup


def slurp(soup):
    days = {}
    parts = [x for x in soup.find_all('a') if '/day/' in x['href']]
    for part in parts:
        n = int(part.contents[0])
        two = int(part.find("span", class_="stats-both").contents[0])
        oneonly = int(part.find("span", class_="stats-firstonly").contents[0])
        one = oneonly + two
        days[n] = (one, two)

    return days


def main(argv):
    day = int(argv[1]) if len(argv) > 1 else aocd.get.current_day()
    year = int(argv[2]) if len(argv) > 2 else aocd.get.most_recent_year()

    days = slurp(_soup(URL.format(year=year)))

    one, two = days.get(day, (0, 0))
    print(f'* {one}, ** {two}')


if __name__ == '__main__':
    main(sys.argv)
