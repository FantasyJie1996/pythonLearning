# -*- coding:utf-8 -*-

from MD5_test import get_card_list
import json

url = 'http://ec.upiot.net/api/v2/1b5771d34b9096e54ca005fa394111ce7d01b894/card/89860619100052819770/?_sign=35de6ff58ff3eee77d8941d1d62b2e00'


response = get_card_list(url)
print(response)
print(type(response))
di = json.loads(response)
print(json.dumps(di,sort_keys=True,indent=2,separators=(',', ':'),ensure_ascii=False))