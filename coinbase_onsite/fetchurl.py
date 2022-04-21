from traceback import print_tb
import requests
import json

# target = 'https://api.pro.coinbase.com/products/BTC-USD/ticker'
target = 'https://api.pro.coinbase.com/products'
respone = requests.get(url=target)

response_dic = json.loads(respone.text)

for item in response_dic:
    print(item['id'])


# json_dic = respone.json()

# for k, v in json_dic.items():
#     print(k, v)
