from re import finditer, M

import requests
from bs4 import BeautifulSoup

from Patern import PATTERN
from url import URl


def parsed_info() -> BeautifulSoup.text:
    return BeautifulSoup(requests.get(URl).text, "html.parser")


def get_data():
    a = []
    page = parsed_info()
    content_info = str(page.find('div', class_='mw-content-ltr'))
    res = finditer(PATTERN, content_info, flags=M)
    for i in res:
        a.append((i.group(1), i.group(2)))
    return a


def create_data_file():
    with open("parsed_site", "w") as file:
        a = get_data()
        for i in a:
            reader = f"{i} \n"
            file.writelines(reader)


if __name__ == '__main__':
    create_data_file()
