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
            links.append(re.search(r'href="(.*?)"', result[0]).group(1))
    print(links)


parse_league_link()
