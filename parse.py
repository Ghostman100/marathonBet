import requests
import re
import json


def login():
    print('Введи пароль')
    # password = input()
    password = 'qweasdzxc123'
    payload = {'login': 'NatashaBet', 'login_password': password,
               'loginUrl': 'https://www.marathonbet.com:443/su/login.htm'}
    response = requests.post("https://www.marathonbet.com/su/login.htm", data=payload)
    print(response.text)
    print()
    print()
    cookie = response.cookies
    return cookie


def bet(cookie):
    payload = {'p': 'SINGLES',
               'b': '[{"url":"7083402,Set_{0}__game_{1}3.RG_A","stake":15,"vip":false,"ew":false}]',
               'choices': '[{"selectionUid":"7083402,Set_{0}__game_{1}3.RG_A","cfId":"7083583","eprice":1.25}]'}
    url = 'https://www.marathonbet.com/su/betslip/placebet2.htm'
    response = requests.post(url, payload, cookies=cookie)
    print(response)
    print()
    print(json.loads(response.text))
    mes = json.loads(response.text)['messages'][0]
    pl = {
        't': mes
    }
    res1 = requests.post('https://www.marathonbet.com/su/betslip/placeticket2.htm', pl)
    print(res1)
    print()
    print(res1.text)


def add_bet(cookie):
    payload = {
        'ch': '{"sn":"Победа Понше, Джессика","mn":"Сет 1, гейм 5","ewc":"1/1 1","cid":32256814884,"prt":"CP","ewf":"1.0","epr":"1.31","prices":{"0":"31/100","1":"1.31","2":"-323","3":"0.31","4":"0.31","5":"-3.23"},"mid":"7083402","u":"7083402,Set_{0}__game_{1}3.RG_A","en":"С.Валтерт - Д.Понше","l":true}',
        'url': 'https://www.marathonbet.com/su/live/7947156',
        'ws': 'true'}
    url = 'https://www.marathonbet.com/su/betslip/add2.htm'
    response = requests.post(url, payload, cookies=cookie)
    print(response)
    print()
    print(response.text)
    bet(cookie)

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

    def matches_links(league_id):
        link = "https://www.marathonbet.com/su/live/" + league_id
        response = requests.get(link)
        html = response.text
        result = re.findall(r'(?sm)<table class="member-area-content-table  "(.*?)</table>', html)
        match_ids = []
        for id in result:
            match_ids.append(re.search(r'<div data-favorites-selector="(.*?)"', id).group(1))
        print(match_ids)

    # links = parse_league_link()
    # matches_links(links[0])


cook = login()
add_bet(cook)
