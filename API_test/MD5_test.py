# -*- coding:utf-8 -*-

import hashlib
import requests
import json

def md5_create(secret):
    #secret = input("input secret:")
    md = hashlib.md5()
    md.update(secret.encode('utf-8'))
    print(md.hexdigest())

url = 'http://ec.upiot.net/api/v2/1b5771d34b9096e54ca005fa394111ce7d01b894/card_no_list/?_sign=35de6ff58ff3eee77d8941d1d62b2e00'

def get_card_list(url):
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url,headers=headers)

    return response.text.encode('utf-8').decode('unicode_escape')

if __name__ == "__main__":
    list_card = get_card_list(url)
    print(list_card)
    dict_card = json.loads(list_card)
    print(len(dict_card["data"]["rows"]))

    with open("./card_list",'w') as f:
        f.write(list_card)