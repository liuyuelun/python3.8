import requests
import json
import threading
#创建一个锁对象
lock = threading.Lock()

def draw():
    n=0
    t50 = 0
    t100 = 0
    while n < 2000:
        url = "https://api-test.timo.team/timo/basic/active/user/draw"

        payload = "{}"
        headers = {
          'Host': 'api-test.timo.team',
          'userlocale': 'in-ID',
          'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ7XCJhcHBUeXBlXCI6XCJhbmRyb2lkXCIsXCJpbnZhbGlkXCI6ZmFsc2UsXCJ1c2VySWRcIjoxMDI2LFwidmVyc2lvblwiOlwiMS4wXCJ9IiwiZXhwIjoxNjc4NDEzNjI3LCJ0b2tlbl90eXBlIjoibm9ybWFsIiwiaWF0IjoxNjc3ODA4ODI3fQ.2y3VgykOsJb0EZrc9vC9yGnVdGi4DA9eD_q_1IfP_iQ',
          'user-agent': 'Mozilla/5.0 (Linux; Android 11; Pixel 3 XL Build/RQ3A.211001.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36',
          'proxyheader': 'eyJjaGVjayI6IjZCRTQ4QzJBNkEyRDFBM0E4NjAwOTJGRDU1RDE0NTVCIiwidXNlcklkIjoxMDI2LCJ1c2VyTG9jYWxlIjoiaW4tSUQiLCJ2ZXJzaW9uIjoiMS4wIn0=',
          'content-type': 'application/json;charset=UTF-8',
          'accept': '*/*',
          'origin': 'https://support-test.timo.team',
          'x-requested-with': 'cool.timo.android',
          'sec-fetch-site': 'same-site',
          'sec-fetch-mode': 'cors',
          'sec-fetch-dest': 'empty',
          'referer': 'https://support-test.timo.team/',
          'accept-language': 'zh-CN,zh;q=0.9,id-ID;q=0.8,id;q=0.7,zh-TW;q=0.6,vi-VN;q=0.5,vi;q=0.4,th-TH;q=0.3,th;q=0.2,ko-KP;q=0.1,ko;q=0.1,en-US;q=0.1,en;q=0.1,ms-MY;q=0.1,ms;q=0.1,ja-JP;q=0.1,ja;q=0.1'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        tp = response.json()["data"]["award"]["type"]
        tp_num = response.json()["data"]["award"]["num"]
        if tp == "diamond" and int(tp_num) == 50:
            t50 +=1
        if tp == "diamond" and int(tp_num) == 100:
            t100 += 1
        print(n)
        n+=1
    print("50钻石的概率：%f"%(t50/n))
    print("100钻石的概率：%f"%(t100/n))
def loop():
    """
    url = "https://active-sandbox.lita.gg/act/loop/teamGold/operate?id=36&operateType=true"

    payload = {}
    headers = {
        'Host': 'active-sandbox.lita.gg',
        'proxyheader': 'eyJjaGVjayI6IjQwMzA5MzE2NTMyREJGMzAxMDY0QTZGRDk1MUQ2M0U3IiwiY2l0eSI6Imhvbmdfa29uZyIsInJlZ2lvbiI6IkhLIiwidGltZSI6MTY4ODQ1MTgwNzA1NSwidXNlcklkIjoyMDM1LCJ1c2VyTG9jYWxlIjoiaW4tSUQiLCJ2ZXJzaW9uIjoiMi4wIn0',
        'accept': '*/*',
        'appplat': 'Web',
        'appversion': '2.0.0',
        'locale': 'in',
        'accesstoken': 'ritfHH5oGNL0649XkYJct6MXnvWlLHzq12jocQahfALXHYbk2dPMQgPAMp5vV5ZK',
        'accept-language': 'zh-CN,zh-Hans;q=0.9',
        'devicetoken': '',
        'origin': 'https://h5-test.lita.gg',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
        'referer': 'https://h5-test.lita.gg/',
        'userlocale': 'in'
    }

    response1 = requests.request("GET", url, headers=headers, data=payload)

    print(response1.text)
    url = "https://active-sandbox.lita.gg/act/loop/teamGold/operate?id=37&operateType=true"

    payload = {}
    headers = {
        'Host': 'active-sandbox.lita.gg',
        'proxyheader': 'eyJjaGVjayI6IjQwMzA5MzE2NTMyREJGMzAxMDY0QTZGRDk1MUQ2M0U3IiwiY2l0eSI6Imhvbmdfa29uZyIsInJlZ2lvbiI6IkhLIiwidGltZSI6MTY4ODQ1MTgwNzA1NSwidXNlcklkIjoyMDM1LCJ1c2VyTG9jYWxlIjoiaW4tSUQiLCJ2ZXJzaW9uIjoiMi4wIn0',
        'accept': '*/*',
        'appplat': 'Web',
        'appversion': '2.0.0',
        'locale': 'in',
        'accesstoken': 'ritfHH5oGNL0649XkYJct6MXnvWlLHzq12jocQahfALXHYbk2dPMQgPAMp5vV5ZK',
        'accept-language': 'zh-CN,zh-Hans;q=0.9',
        'devicetoken': '',
        'origin': 'https://h5-test.lita.gg',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
        'referer': 'https://h5-test.lita.gg/',
        'userlocale': 'in'
    }

    response2 = requests.request("GET", url, headers=headers, data=payload)

    print(response2.text)

    s = 7483

    print("第一名奖励是%s"%(0.15*s))
    print("第二名奖励是%s"%(0.11*s))
    print("第三名奖励是%s"%(0.09*s))
    print("第4~7名奖励是%s"%(0.07*s))
    print("第8~10名奖励是%s"%(0.04*s))
    print("第11~15名奖励是%s"%(0.03*s))
    print("第16~20名奖励是%s"%(0.02*s))
    """
    l = []
    import requests

    url = "http://api-test.funbit.me/funbit/v2/player/recommend/batch?batchNo=&countryIsoCode=&page=1&rows=50"

    payload = {}
    headers = {
        'Host': 'api-test.funbit.me',
        'Cookie': 'JSESSIONID=24A43598C62EB3029A66D04E833FDF1F',
        'userLocale': 'en',
        'User-Agent': 'LitaDev/1.140 (but.lita.ios; build:1; iOS 15.4.0) Alamofire/5.6.4',
        'dataRangerBddid': 'EID4QVV6YSXEXKIXAED33Z6W5JHDX4AVJFOZT4BB6QXEZBXCCSIA01',
        'hasProxy': 'false',
        'deviceToken': '647D376F2B2A50BD7500FFE9E90E5F88',
        'appVersion': '1.140',
        'iosSystemVersion': '15.4',
        'locale': 'en',
        'AccessToken': '',
        'proxyHeader': 'eyJjaGVjayI6IkJCQkE5RkQwRTg1RTYxRUM3RjE0MDA5RDYwN0EyOThEIiwiY2l0eSI6Imhvbmdfa29uZyIsInJlZ2lvbiI6IkhLIiwidGltZSI6MTY4ODYyNzcwMTMxOCwidXNlckxvY2FsZSI6ImVuLUNOIiwidmVyc2lvbiI6IjIuMCJ9',
        'dataRangerSsid': '69109df5-3498-460e-be72-46b5615e912d',
        'Accept-Language': 'zh-Hans-ID;q=1.0, id-ID;q=0.9, ko-ID;q=0.8, ms-ID;q=0.7, en-ID;q=0.6, vi-ID;q=0.5',
        'zoneId': 'Asia/Shanghai',
        'timeZoneOffset': '28800000',
        'appPlat': 'IOS',
        'hasSim': 'false',
        'shumeiDeviceId': '20220506142108cd827659e7ae94052c86774d30d266b4017189740c3358e4',
        'cuteness': 'AACSBwKgbfj9D9avixYW2p4rT8Lfb0/U3ywA2sd9X8jPbV3NzWlczM9uXcCeO1XKymlYwZhoDJ3Ea13NzzxVzspoWZzObwnKy2kPzM1uWsnFZlrMzTxey8hnCMzfIg==',
        'Accept': '*/*'
    }

    playerlist = requests.request("GET", url, headers=headers, data=payload)
    if playerlist.status_code != 200:
        print("请求失败，错误码是%s"%(playerlist.status_code))
    if playerlist.json()["status"] != "0":
        print("接口返回异常%s"%(playerlist.text))
    pl = playerlist.json()["data"]["rows"]

    for i in range(0,len(pl)):
        print(i)
        l .append(pl[i]["id"])

    for i in l:
        url = "http://api-test.funbit.me//litamsg/improxy/sendPrivateMsg"

        payload = json.dumps({
            "ext": "{\"memeType\":\"-1\",\"playStatus\":false,\"memeName\":\"emoji_cloth\",\"memePic\":\"\",\"id\":\"-3\",\"lottieUrl\":\"\",\"memeIcon\":\"emoji_guess.png\",\"unLockDes\":\"\",\"lock\":false}",
            "appVersion": "1.140",
            "receiverId": i,
            "source": "tencent",
            "receiverIds": [
                i
            ],
            "content": "[表情]",
            "messageType": "EMOJI_CHAT",
            "currentTime": 1688627807372,
            "message": {
                "chatMessageType": 0,
                "chatBubble": "{\"area\":\"chat\",\"userId\":\"1637\"}",
                "content": "[表情]"
            },
            "functionType": "EMOJI_CHAT_MESSAGE",
            "senderId": 1637,
            "messageId": "-NZe2sBVMwdiacKxD1aA",
            "os": "IOS",
            "sourceType": "private_msg"
        })
        headers = {
            'Host': 'api-test.funbit.me',
            'hasProxy': 'false',
            'signStr': 'MTYzNzE2ODg2Mjc4MDczODY=',
            'userLocale': 'in',
            'User-Agent': 'LitaDev/1.140 (but.lita.ios; build:1; iOS 15.4.0) Alamofire/5.6.4',
            'dataRangerBddid': 'EID4QVV6YSXEXKIXAED33Z6W5JHDX4AVJFOZT4BB6QXEZBXCCSIA01',
            'Accept': '*/*',
            'deviceToken': '647D376F2B2A50BD7500FFE9E90E5F88',
            'appVersion': '1.140',
            'iosSystemVersion': '15.4',
            'locale': 'in',
            'AccessToken': 'WeCg9mA1oJ/miq3ac3xZOzWewEIxi+7MEuy7BQuZ+2IiKPdZSOZ0wRXmQU1reqxX',
            'sign': 'a8d7920271f0bc3f84ed27323448fb7a',
            'proxyHeader': 'eyJjaGVjayI6IjE1REJCMTlCNjM0RUZFNDg0RUYyNkJEODM0MkIzNDcwIiwiY2l0eSI6Imhvbmdfa29uZyIsInJlZ2lvbiI6IkhLIiwidGltZSI6MTY4ODYyNzgwNTI4MiwidXNlcklkIjoxNjM3LCJ1c2VyTG9jYWxlIjoiaW4tSUQiLCJ2ZXJzaW9uIjoiMi4wIn0=',
            'dataRangerSsid': '69109df5-3498-460e-be72-46b5615e912d',
            'timeStamp': '1688627807386',
            'Accept-Language': 'zh-Hans-ID;q=1.0, id-ID;q=0.9, ko-ID;q=0.8, ms-ID;q=0.7, en-ID;q=0.6, vi-ID;q=0.5',
            'zoneId': 'Asia/Shanghai',
            'timeZoneOffset': '28800000',
            'appPlat': 'IOS',
            'hasSim': 'false',
            'Content-Type': 'application/json',
            'playerState': '1',
            'cuteness': 'AADtFeXEEuoaawSMQ1ZpyHlPMNA4CzDGOEh/yCAZINooCSLfKg0j3igKItJ5XyrYLQ0n038Mc48jDyLfKFgq3C0MJo4pC3bYLA1w3ioKJdsiAiXeKlgh2S8Dd944Rg==',
            'shumeiDeviceId': '20220506142108cd827659e7ae94052c86774d30d266b4017189740c3358e4'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

def write_file():
    global lock
    with lock:
        with open("threadlock.txt","a") as f:
            f.write("Threading 1:Writing something to the file")
def read_file():
    global lock
    with lock:
        with open("threadlock.txt","r") as f:
            content = f.read()
            print("Threading 2: read content from the file")
            print(content)
def thread_start():
    thread1 = threading.Thread(target=write_file)
    thread2 = threading.Thread(target=read_file)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("Both threads have finished!")

if __name__ == '__main__':
    thread_start()