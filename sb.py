import requests as rq
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input", help="input the string you want to translate")
args = parser.parse_args()

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
data={
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "16496469253566",
    "sign": "91717c37bb6d4d338e4f7c04d85446d5",
    "lts": "1649646925356",
    "bv": "7e897500afcde4988ba75227fa754c55",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTlME"
}
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
}
data['i'] = args.input
rp = rq.post(url=url,data=data,headers=head)
name = rp.json()
print(name['translateResult'][0][0]['tgt'])