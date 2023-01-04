import time
from time import sleep

import requests
import json
import requests

header = {
  'Host': 'api-test.funbit.me',
  'userLocale': 'in',
  'User-Agent': 'FunbitDev/1.114 (but.lita.ios; build:1; iOS 15.4.0) Alamofire/5.2.2',
  'dataRangerBddid': 'EID4QVV6YSXEXKIXAED33Z6W5JHDX4AVJFOZT4BB6QXEZBXCCSIA01',
  'hasProxy': 'false',
  'deviceToken': '647D376F2B2A50BD7500FFE9E90E5F88',
  'appVersion': '1.114',
  'iosSystemVersion': '15.4',
  'locale': 'in',
  'AccessToken': 'u/CKsSa3VMhXEXYGt4VeZVtGbyb428fZVSng40i2xqyhNAH10kWDz7xdrAR4P1CM',
  'proxyHeader': 'eyJjaGVjayI6IkRENUJEM0E0ODdGNTg2NUY2MDNDODgyNTI5Nzg0RkMxIiwiY2l0eSI6Imhvbmdfa29uZyIsInJlZ2lvbiI6IkhLIiwidGltZSI6MTY3MjczNzQ1MDAwNiwidXNlcklkIjoxNjM1LCJ1c2VyTG9jYWxlIjoiaW4tSUQiLCJ2ZXJzaW9uIjoiMi4wIn0=',
  'dataRangerSsid': '98b41a2b-3f67-4b38-9f1a-f304f089df14',
  'Accept-Language': 'zh-Hans-ID;q=1.0, vi-ID;q=0.9, id-ID;q=0.8, ms-ID;q=0.7, th-ID;q=0.6, ko-ID;q=0.5',
  'zoneId': 'Asia/Shanghai',
  'timeZoneOffset': '28800000',
  'appPlat': 'IOS',
  'hasSim': 'false',
  'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
  'shumeiDeviceId': '20220506142108cd827659e7ae94052c86774d30d266b4017189740c3358e4',
  'playerState': '1',
  'Accept': '*/*'
}
url = "http://api-test.funbit.me/litaroom/v2/voiceroom/inRoom"

payload = "roomId=2000"
headers = header

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)

url = "http://api-test.funbit.me/litaroom/v2/voiceroom/inRoomCallback"

payload = "roomId=2000"
headers = header

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)

while True:
    time.sleep(5)
    import requests
    import json

    url = "http://api-test.funbit.me/litaroom/v2/voiceroom/onroom"

    payload = json.dumps({
        "micIndex": "-1",
        "userId": "1635",
        "roomId": "2000",
        "state": "0"
    })
    headers = header

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
