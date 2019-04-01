import requests
import re
import json


def login():
    print('Введи пароль')
    password = input()
    payload = {'login': 'NatashaBet', 'login_password': password,
               'loginUrl': 'https://www.marathonbet.com:443/su/login.htm'}
    response = requests.post("https://www.marathonbet.com/su/login.htm", data=payload)
    print(response.text)
    print()
    print()
    print(response.cookies)


def parse_league_link():
    response = requests.get("https://www.marathonbet.com/su/live/1372932")
    html = response.text
    result = re.findall(r'(?sm)<a class="category-label-link"(.+?)</a>', html)
    links = []
    for link in result:
        game = re.search(r'Dota 2', link)
        if game:
            links.append(re.search(r'href=" /su/live/(.*?)"', result[0]).group(1))
    print(links)
    return links


def matchs_links(league_id):
    link = "https://www.marathonbet.com/su/live/" + league_id
    response = requests.get(link)
    html = response.text
    result = re.findall(r'(?sm)<table class="member-area-content-table  "(.*?)</table>', html)
    match_ids = []
    for id in result:
        match_ids.append(re.search(r'<div data-favorites-selector="(.*?)"',id).group(1))
    print(match_ids)


links = parse_league_link()
matchs_links(links[0])
