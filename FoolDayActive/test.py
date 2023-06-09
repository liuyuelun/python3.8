import threading
import time
import requests

def xinling():
    while True:
        for id in ["1635","1637"]:
            url = "http://api-test.funbit.me/funbit/v2/api/player/testPlayerIdentityCommandMsg?userId="+id

            payload = {}
            headers = {
                'AccessToken': 'WeCg9mA1oJ/miq3ac3xZOxIYnqxkaYRzXr4a598hZ7ASQ3a/khWAXfkd27fPjTwo',
                'Cookie': 'JSESSIONID=EBE11002571272B33016CE44B1B265EF'
            }

            response = requests.request("GET", url, headers=headers, data=payload)

            print(response.text)
        time.sleep(30)
def litateam():
    for id in ["1635","1637"]:
        url = "http://api-test.funbit.me/funbit/v2/api/player/testPlayerIdentityMsg?userId="+id

        payload = {}
        headers = {
            'AccessToken': 'WeCg9mA1oJ/miq3ac3xZOxIYnqxkaYRzXr4a598hZ7ASQ3a/khWAXfkd27fPjTwo',
            'Cookie': 'JSESSIONID=EBE11002571272B33016CE44B1B265EF'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)
def testsvipbox():
    g6760 = 0
    g6759 = 0
    g6758 = 0
    g6778 = 0
    g6757 = 0
    g6756 = 0
    g6779 = 0
    g6755 = 0
    m=100
    count = 999
    alltime = m*count
    for i in range(1,m+1):
        import requests
        import json

        url = "http://api-test.funbit.me/litabasic/active/treasureBoxGift/openBoxAward"

        payload = json.dumps({
            "clickCount": "1",
            "roomId": "0",
            "combo": "1",
            "boxGiftId": "6771",
            "count": count,
            "targetIds": "1635",
            "comboId": "1685331501381163727566040"
        })
        headers = {
            'Host': 'api-test.funbit.me',
            'hasProxy': 'false',
            'signStr': 'MTYzNzE2ODUzMzE1MDE0MjY=',
            'userLocale': 'in',
            'User-Agent': 'FunbitDev/1.133 (but.lita.ios; build:1; iOS 15.4.0) Alamofire/5.6.4',
            'dataRangerBddid': 'EID4QVV6YSXEXKIXAED33Z6W5JHDX4AVJFOZT4BB6QXEZBXCCSIA01',
            'Accept': '*/*',
            'deviceToken': '647D376F2B2A50BD7500FFE9E90E5F88',
            'appVersion': '1.133',
            'iosSystemVersion': '15.4',
            'locale': 'in',
            'AccessToken': 'WeCg9mA1oJ/miq3ac3xZO+U48T5S2k8w5XDdsdK4ed9coawdKNBx56ft9HGfYZUz',
            'sign': '71792c1ab7b3391d3c8e596bdd5fe19a',
            'proxyHeader': 'eyJjaGVjayI6Ijc3QkUzOUVEMDM1QUYzQjhDM0I4NzAxMDIyOTc5NEIwIiwiY2l0eSI6Imhvbmdfa29uZyIsInJlZ2lvbiI6IkhLIiwidGltZSI6MTY4NTMzMTQxOTgxMywidXNlcklkIjoxNjM3LCJ1c2VyTG9jYWxlIjoiaW4tSUQiLCJ2ZXJzaW9uIjoiMi4wIn0=',
            'dataRangerSsid': '69109df5-3498-460e-be72-46b5615e912d',
            'timeStamp': '1685331501426',
            'Accept-Language': 'zh-Hans-ID;q=1.0, id-ID;q=0.9, vi-ID;q=0.8, th-ID;q=0.7, ko-ID;q=0.6, ms-ID;q=0.5',
            'zoneId': 'Asia/Shanghai',
            'timeZoneOffset': '28800000',
            'appPlat': 'IOS',
            'hasSim': 'false',
            'Content-Type': 'application/json',
            'shumeiDeviceId': '20220506142108cd827659e7ae94052c86774d30d266b4017189740c3358e4',
            'playerState': '1',
            'cuteness': 'AABhPT97nsLA1BRPc6Dl4KPwvPjitLzu4vfz4PqmrPLytq738LKv9vK1rvqj4Kbw97Kr+6Wz/6f5sK738uem9PezqqbztPrw9rL89vC1qfP4van28Oet8fW8+/bi+Q=='
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        if response.json()["status"] != "0":
            print(response.json())

        svipbox = response.json()["data"]["giftAttach"]["awards"]
        for n in range(0,len(svipbox)):
            if svipbox[n]["giftId"] == "6760":
                g6760 += int(svipbox[n]["giftCount"])
                print(svipbox[n]["giftId"],g6760)
            elif svipbox[n]["giftId"] == "6759":
                g6759 += int(svipbox[n]["giftCount"])
                print(svipbox[n]["giftId"], g6759)
            elif svipbox[n]["giftId"] == "6758":
                g6758 += int(svipbox[n]["giftCount"])
                print(svipbox[n]["giftId"], g6758)
            elif svipbox[n]["giftId"] == "6778":
                g6778 += int(svipbox[n]["giftCount"])
                print(svipbox[n]["giftId"], g6778)
            elif svipbox[n]["giftId"] == "6757":
                g6757 += int(svipbox[n]["giftCount"])
                print(svipbox[n]["giftId"], g6757)
            elif svipbox[n]["giftId"] == "6756":
                g6756 += int(svipbox[n]["giftCount"])
                print(svipbox[n]["giftId"], g6756)
            elif svipbox[n]["giftId"] == "6779":
                g6779 += int(svipbox[n]["giftCount"])
                print(svipbox[n]["giftId"], g6779)
            elif svipbox[n]["giftId"] == "6755":
                g6755 += int(svipbox[n]["giftCount"])
                print(svipbox[n]["giftId"], g6755)
            else:
                print(svipbox["giftId"])
    if g6760 != 0:
        print("宝箱中礼物g6760(%s)的概率是%s" % (g6760,g6760 / alltime))
    else:
        print("未抽中g6760")
    if g6759 != 0:
        print("宝箱中礼物g6759(%s)的概率是%s" % (g6759,g6759 / alltime))
    else:
        print("未抽中g6759")
    if g6758 != 0:
        print("宝箱中礼物g6758(%s)的概率是%s"%(g6758,g6758/alltime))
    else:
        print("未抽中g6758")
    if g6778 != 0:
        print("宝箱中礼物g6778(%s)的概率是%s"%(g6778,g6778/alltime))
    else:
        print("未抽中g6778")
    if g6757 != 0:
        print("宝箱中礼物g6757(%s)的概率是%s"%(g6757,g6757/alltime))
    else:
        print("未抽中g6757")
    if g6756 != 0:
        print("宝箱中礼物g6756(%s)的概率是%s"%(g6756,g6756/alltime))
    else:
        print("未抽中g6756")
    if g6779 != 0:
        print("宝箱中礼物g6779(%s)的概率是%s" % (g6779,g6779 / alltime))
    else:
        print("未抽中g6779")
    if g6755 != 0:
        print("宝箱中礼物g6755(%s)的概率是%s"%(g6755,g6755/alltime))
    else:
        print("未抽中g6755")
def testboxinvip():
    g6044 = 0
    g6046 = 0
    g6047 = 0
    g6049 = 0
    g6771 = 0
    g6050 = 0
    g6051 = 0
    g6052 = 0
    g6153 = 0
    g6154 = 0

    m=10
    count = 999
    alltime = m*count
    for i in range(1,m+1):
        import requests
        import json

        url = "http://api-test.funbit.me/litabasic/active/treasureBoxGift/openBoxAward"

        payload = json.dumps({
            "clickCount": "1",
            "roomId": "0",
            "combo": "1",
            "boxGiftId": "6155",
            "count": str(count),
            "targetIds": "1635",
            "comboId": "1685331501381163727566040"
        })
        headers = {
            'Host': 'api-test.funbit.me',
            'hasProxy': 'false',
            'signStr': 'MTYzNzE2ODUzMzE1MDE0MjY=',
            'userLocale': 'in',
            'User-Agent': 'FunbitDev/1.133 (but.lita.ios; build:1; iOS 15.4.0) Alamofire/5.6.4',
            'dataRangerBddid': 'EID4QVV6YSXEXKIXAED33Z6W5JHDX4AVJFOZT4BB6QXEZBXCCSIA01',
            'Accept': '*/*',
            'deviceToken': '647D376F2B2A50BD7500FFE9E90E5F88',
            'appVersion': '1.133',
            'iosSystemVersion': '15.4',
            'locale': 'in',
            'AccessToken': 'WeCg9mA1oJ/miq3ac3xZO+U48T5S2k8w5XDdsdK4ed9coawdKNBx56ft9HGfYZUz',
            'sign': '71792c1ab7b3391d3c8e596bdd5fe19a',
            'proxyHeader': 'eyJjaGVjayI6Ijc3QkUzOUVEMDM1QUYzQjhDM0I4NzAxMDIyOTc5NEIwIiwiY2l0eSI6Imhvbmdfa29uZyIsInJlZ2lvbiI6IkhLIiwidGltZSI6MTY4NTMzMTQxOTgxMywidXNlcklkIjoxNjM3LCJ1c2VyTG9jYWxlIjoiaW4tSUQiLCJ2ZXJzaW9uIjoiMi4wIn0=',
            'dataRangerSsid': '69109df5-3498-460e-be72-46b5615e912d',
            'timeStamp': '1685331501426',
            'Accept-Language': 'zh-Hans-ID;q=1.0, id-ID;q=0.9, vi-ID;q=0.8, th-ID;q=0.7, ko-ID;q=0.6, ms-ID;q=0.5',
            'zoneId': 'Asia/Shanghai',
            'timeZoneOffset': '28800000',
            'appPlat': 'IOS',
            'hasSim': 'false',
            'Content-Type': 'application/json',
            'shumeiDeviceId': '20220506142108cd827659e7ae94052c86774d30d266b4017189740c3358e4',
            'playerState': '1',
            'cuteness': 'AABhPT97nsLA1BRPc6Dl4KPwvPjitLzu4vfz4PqmrPLytq738LKv9vK1rvqj4Kbw97Kr+6Wz/6f5sK738uem9PezqqbztPrw9rL89vC1qfP4van28Oet8fW8+/bi+Q=='
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        if response.json()["status"] != "0":
            print(response.json())
        svipbox = response.json()["data"]["giftAttach"]["awards"]
        for n in range(0,len(svipbox)):
            if svipbox[n]["giftId"] == "6044":
                g6044 += int(svipbox[n]["giftCount"])
                print(svipbox[n]["giftId"],g6044)
            elif svipbox[n]["giftId"] == "6046":
                g6046 += int(svipbox[n]["giftCount"])
                print(svipbox[n]["giftId"],g6046)
            elif svipbox[n]["giftId"] == "6047":
                g6047 += int(svipbox[n]["giftCount"])
                print(svipbox[n]["giftId"], g6047)
            elif svipbox[n]["giftId"] == "6049":
                g6049 += int(svipbox[n]["giftCount"])
                print(svipbox[n]["giftId"], g6049)
            elif svipbox[n]["giftId"] == "6771":
                g6771 += int(svipbox[n]["giftCount"])
                print(svipbox[n]["giftId"], g6771)
            elif svipbox[n]["giftId"] == "6050":
                g6050 += int(svipbox[n]["giftCount"])
                print(svipbox[n]["giftId"], g6050)
            elif svipbox[n]["giftId"] == "6051":
                g6051 += int(svipbox[n]["giftCount"])
                print(svipbox[n]["giftId"], g6051)
            elif svipbox[n]["giftId"] == "6052":
                g6052 += int(svipbox[n]["giftCount"])
                print(svipbox[n]["giftId"], g6052)
            elif svipbox[n]["giftId"] == "6153":
                g6153 += int(svipbox[n]["giftCount"])
                print(svipbox[n]["giftId"], g6153)
            elif svipbox[n]["giftId"] == "6154":
                g6154 += int(svipbox[n]["giftCount"])
                print(svipbox[n]["giftId"], g6154)
            else:
                print(svipbox[n]["giftId"])
    if g6044 != 0:
        print("宝箱中礼物g6044(%s)的概率是%s"%(g6044,g6044/alltime))
    else:
        print("未抽中g6044")
    if g6046 != 0:
        print("宝箱中礼物g6046(%s)的概率是%s"%(g6046,g6046/alltime))
    else:
        print("未抽中g6046")
    if g6047 != 0:
        print("宝箱中礼物g6047(%s)的概率是%s" % (g6047,g6047/alltime))
    else:
        print("未抽中g6047")
    if g6049 != 0:
        print("宝箱中礼物g6049(%s)的概率是%s" % (g6049,g6049/alltime))
    else:
        print("未抽中g6049")
    if g6771 != 0:
        print("宝箱中礼物g6771(%s)的概率是%s" % (g6771,g6771/alltime))
    else:
        print("未抽中g6771")
    if g6050 != 0:
        print("宝箱中礼物g6050(%s)的概率是%s" % (g6050,g6050 / alltime))
    else:
        print("未抽中g6050")
    if g6051 != 0:
        print("宝箱中礼物g6051(%s)的概率是%s" % (g6051,g6051 / alltime))
    else:
        print("未抽中g6051")
    if g6052 != 0:
        print("宝箱中礼物g6052(%s)的概率是%s" % (g6052,g6052 / alltime))
    else:
        print("未抽中g6052")
    if g6153 != 0:
        print("宝箱中礼物g6153(%s)的概率是%s" % (g6153,g6153 / alltime))
    else:
        print("未抽中g6153")
    if g6154 != 0:
        print("宝箱中礼物g6154(%s)的概率是%s" % (g6154,g6154 / alltime))
    else:
        print("未抽中g6154")
def testboxnotvip():
    g6044 = 0
    g6046 = 0
    g6047 = 0
    g6049 = 0
    g6152 = 0
    g6050 = 0
    g6051 = 0
    g6052 = 0
    g6153 = 0
    g6154 = 0

    m=100
    count = 999
    alltime = m*count
    for i in range(1,m+1):
        import requests
        import json

        url = "http://api-test.funbit.me/litabasic/active/treasureBoxGift/openBoxAward"

        payload = json.dumps({
            "clickCount": "1",
            "roomId": "0",
            "combo": "1",
            "boxGiftId": "6155",
            "count": count,
            "targetIds": "1635",
            "comboId": "1685331501381163727566040"
        })
        headers = {
            'Host': 'api-test.funbit.me',
            'hasProxy': 'false',
            'signStr': 'MTYzNzE2ODUzMzE1MDE0MjY=',
            'userLocale': 'in',
            'User-Agent': 'FunbitDev/1.133 (but.lita.ios; build:1; iOS 15.4.0) Alamofire/5.6.4',
            'dataRangerBddid': 'EID4QVV6YSXEXKIXAED33Z6W5JHDX4AVJFOZT4BB6QXEZBXCCSIA01',
            'Accept': '*/*',
            'deviceToken': '647D376F2B2A50BD7500FFE9E90E5F88',
            'appVersion': '1.133',
            'iosSystemVersion': '15.4',
            'locale': 'in',
            'AccessToken': 'GffMt9u+3Qi6J5wukt0522l7fA1ZmWnpyaiZn8bSqBg6dRwq81PxGtYQ/NAHOrK8',
            'sign': '71792c1ab7b3391d3c8e596bdd5fe19a',
            'proxyHeader': 'eyJjaGVjayI6Ijc3QkUzOUVEMDM1QUYzQjhDM0I4NzAxMDIyOTc5NEIwIiwiY2l0eSI6Imhvbmdfa29uZyIsInJlZ2lvbiI6IkhLIiwidGltZSI6MTY4NTMzMTQxOTgxMywidXNlcklkIjoxNjM3LCJ1c2VyTG9jYWxlIjoiaW4tSUQiLCJ2ZXJzaW9uIjoiMi4wIn0=',
            'dataRangerSsid': '69109df5-3498-460e-be72-46b5615e912d',
            'timeStamp': '1685331501426',
            'Accept-Language': 'zh-Hans-ID;q=1.0, id-ID;q=0.9, vi-ID;q=0.8, th-ID;q=0.7, ko-ID;q=0.6, ms-ID;q=0.5',
            'zoneId': 'Asia/Shanghai',
            'timeZoneOffset': '28800000',
            'appPlat': 'IOS',
            'hasSim': 'false',
            'Content-Type': 'application/json',
            'shumeiDeviceId': '20220506142108cd827659e7ae94052c86774d30d266b4017189740c3358e4',
            'playerState': '1',
            'cuteness': 'AABhPT97nsLA1BRPc6Dl4KPwvPjitLzu4vfz4PqmrPLytq738LKv9vK1rvqj4Kbw97Kr+6Wz/6f5sK738uem9PezqqbztPrw9rL89vC1qfP4van28Oet8fW8+/bi+Q=='
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        if response.json()["status"] != "0":
            print(response.json())
        svipbox = response.json()["data"]["giftAttach"]["awards"]
        for n in range(0,len(svipbox)):
            if svipbox[n]["giftId"] == "6044":
                g6044 += int(svipbox[n]["giftCount"])
                print(svipbox[n]["giftId"],g6044)
            elif svipbox[n]["giftId"] == "6046":
                g6046 += int(svipbox[n]["giftCount"])
                print(svipbox[n]["giftId"],g6046)
            elif svipbox[n]["giftId"] == "6047":
                g6047 += int(svipbox[n]["giftCount"])
                print(svipbox[n]["giftId"], g6047)
            elif svipbox[n]["giftId"] == "6049":
                g6049 += int(svipbox[n]["giftCount"])
                print(svipbox[n]["giftId"], g6049)
            elif svipbox[n]["giftId"] == "6152":
                g6152 += int(svipbox[n]["giftCount"])
                print(svipbox[n]["giftId"], g6152)
            elif svipbox[n]["giftId"] == "6050":
                g6050 += int(svipbox[n]["giftCount"])
                print(svipbox[n]["giftId"], g6050)
            elif svipbox[n]["giftId"] == "6051":
                g6051 += int(svipbox[n]["giftCount"])
                print(svipbox[n]["giftId"], g6051)
            elif svipbox[n]["giftId"] == "6052":
                g6052 += int(svipbox[n]["giftCount"])
                print(svipbox[n]["giftId"], g6052)
            elif svipbox[n]["giftId"] == "6153":
                g6153 += int(svipbox[n]["giftCount"])
                print(svipbox[n]["giftId"], g6153)
            elif svipbox[n]["giftId"] == "6154":
                g6154 += int(svipbox[n]["giftCount"])
                print(svipbox[n]["giftId"], g6154)
            else:
                print(svipbox[n]["giftId"])
    if g6044 != 0:
        print("宝箱中礼物g6044(%s)的概率是%s"%(g6044,g6044/alltime))
    else:
        print("未抽中g6044")
    if g6046 != 0:
        print("宝箱中礼物g6046(%s)的概率是%s"%(g6046,g6046/alltime))
    else:
        print("未抽中g6046")
    if g6047 != 0:
        print("宝箱中礼物g6047(%s)的概率是%s" % (g6047,g6047/alltime))
    else:
        print("未抽中g6047")
    if g6049 != 0:
        print("宝箱中礼物g6049(%s)的概率是%s" % (g6049,g6049/alltime))
    else:
        print("未抽中g6049")
    if g6152 != 0:
        print("宝箱中礼物g6152(%s)的概率是%s" % (g6152,g6152/alltime))
    else:
        print("未抽中g6771")
    if g6050 != 0:
        print("宝箱中礼物g6050(%s)的概率是%s" % (g6050,g6050 / alltime))
    else:
        print("未抽中g6050")
    if g6051 != 0:
        print("宝箱中礼物g6051(%s)的概率是%s" % (g6051,g6051 / alltime))
    else:
        print("未抽中g6051")
    if g6052 != 0:
        print("宝箱中礼物g6052(%s)的概率是%s" % (g6052,g6052 / alltime))
    else:
        print("未抽中g6052")
    if g6153 != 0:
        print("宝箱中礼物g6153(%s)的概率是%s" % (g6153,g6153 / alltime))
    else:
        print("未抽中g6153")
    if g6154 != 0:
        print("宝箱中礼物g6154(%s)的概率是%s" % (g6154,g6154 / alltime))
    else:
        print("未抽中g6154")
def buygiftpack():

    m=100
    for i in range(0,m):
        import requests
        time.sleep(2)
        url = "https://active-sandbox.lita.gg/act/slotMachine/buyItem?num=1000"

        payload = {}
        headers = {
            'AccessToken': 'u/CKsSa3VMhXEXYGt4VeZVp/8jXtZ3Qtvwf7bnppZEHpKjeTBE5uhTuR3owX24Ao'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.json())
def activelottery():
    A0=0
    A1=0
    A2=0
    A3=0
    A4=0
    A5=0
    A6=0
    C0=0
    C1=0
    C2=0
    C3=0
    C4=0
    C5=0
    C6=0
    E0=0
    E1=0
    E2=0
    E3=0
    E4=0
    E5=0
    E6=0

    m=10000
    for i in range(0,m):
        import requests

        url = "https://active-sandbox.lita.gg/act/slotMachine/letLottery?num=30"

        payload = {}
        headers = {
            'AccessToken': 'u/CKsSa3VMhXEXYGt4VeZVzqlslCIONGWTvQNXfnXDErrcC7vyhJOYDvMnyFTt5i'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        if response.json()["status"] != "0":
            print(response.json())
            print("循环次数是%s"%(m))
            break
        if  response.status_code != 200:
            print("循环次数是%s"%(m))
            break
        result = response.json()["data"]["lotteryResult"]
        for n in range(0, 3):
            if n == 0:
                if result[n] == "0":
                    A0 +=1
                    print("A0",A0)
                elif result[n] == "1":
                    A1 += 1
                    print("A1", A1)
                elif result[n] == "2":
                    A2 += 1
                    print("A2", A2)
                elif result[n] == "3":
                    A3 += 1
                    print("A3", A3)
                elif result[n] == "4":
                    A4 += 1
                    print("A4", A4)
                elif result[n] == "5":
                    A5 += 1
                    print("A5", A5)
                elif result[n] == "6":
                    A6 += 1
                    print("A6", A6)
            if n == 1:
                if result[n] == "0":
                    C0 += 1
                    print("C0", C0)
                elif result[n] == "1":
                    C1 += 1
                    print("C1", C1)
                elif result[n] == "2":
                    C2 += 1
                    print("C2", C2)
                elif result[n] == "3":
                    C3 += 1
                    print("C3", C3)
                elif result[n] == "4":
                    C4 += 1
                    print("C4", C4)
                elif result[n] == "5":
                    C5 += 1
                    print("C5", C5)
                elif result[n] == "6":
                    C6 += 1
                    print("C6", C6)
            if n == 2:
                if result[n] == "0":
                    E0 += 1
                    print("E0", E0)
                elif result[n] == "1":
                    E1 += 1
                    print("E1", E1)
                elif result[n] == "2":
                    E2 += 1
                    print("E2", E2)
                elif result[n] == "3":
                    E3 += 1
                    print("E3", E3)
                elif result[n] == "4":
                    E4 += 1
                    print("E4", E4)
                elif result[n] == "5":
                    E5 += 1
                    print("E5", E5)
                elif result[n] == "6":
                    E6 += 1
                    print("E6", E6)

    if A0 != 0:
        print("A0(%s)的概率是%s" % (A0, A0/m))
    else:
        print("未抽中A0")
    if A1 != 0:
        print("A1(%s)的概率是%s" % (A1, A1 / m))
    else:
        print("未抽中A1")
    if A2 != 0:
        print("A2(%s)的概率是%s" % (A2, A2 / m))
    else:
        print("未抽中A2")
    if A3 != 0:
        print("A3(%s)的概率是%s" % (A3, A3 / m))
    else:
        print("未抽中A3")
    if A4 != 0:
        print("A4(%s)的概率是%s" % (A4, A4 / m))
    else:
        print("未抽中A4")
    if A5 != 0:
        print("A5(%s)的概率是%s" % (A5, A5 / m))
    else:
        print("未抽中A5")
    if A6 != 0:
        print("A6(%s)的概率是%s" % (A6, A6 / m))
    else:
        print("未抽中A6")
    if C0 != 0:
        print("C0(%s)的概率是%s" % (C0, C0/m))
    else:
        print("未抽中C0")
    if C1 != 0:
        print("C1(%s)的概率是%s" % (C1, C1 / m))
    else:
        print("未抽中C1")
    if C2 != 0:
        print("C2(%s)的概率是%s" % (C2, C2 / m))
    else:
        print("未抽中C2")
    if C3 != 0:
        print("C3(%s)的概率是%s" % (C3, C3 / m))
    else:
        print("未抽中C3")
    if C4 != 0:
        print("C4(%s)的概率是%s" % (C4, C4 / m))
    else:
        print("未抽中C4")
    if C5 != 0:
        print("C5(%s)的概率是%s" % (C5, C5 / m))
    else:
        print("未抽中C5")
    if C6 != 0:
        print("C6(%s)的概率是%s" % (C6, C6 / m))
    else:
        print("未抽中C6")
    if E0 != 0:
        print("E0(%s)的概率是%s" % (E0, E0/m))
    else:
        print("未抽中E0")
    if E1 != 0:
        print("E1(%s)的概率是%s" % (E1, E1 / m))
    else:
        print("未抽中E1")
    if E2 != 0:
        print("E2(%s)的概率是%s" % (E2, E2 / m))
    else:
        print("未抽中E2")
    if E3 != 0:
        print("E3(%s)的概率是%s" % (E3, E3 / m))
    else:
        print("未抽中E3")
    if E4 != 0:
        print("E4(%s)的概率是%s" % (E4, E4 / m))
    else:
        print("未抽中E4")
    if E5 != 0:
        print("E5(%s)的概率是%s" % (E5, E5 / m))
    else:
        print("未抽中E5")
    if E6 != 0:
        print("E6(%s)的概率是%s" % (E6, E6 / m))
    else:
        print("未抽中E6")
def testmany():
    import requests
    import concurrent.futures

    # 定义目标测试接口的URL
    url = "https://active-sandbox.lita.gg/act/slotMachine/letLottery?num=1"

    # 定义要发送的请求数据（根据接口需要进行相应配置）
    payload = {
    }
    headers = {
        'AccessToken': 'WeCg9mA1oJ/miq3ac3xZO7zmK0kxv4rL+ag9bs+6KJZ6CdvU8vjzmn4+OARDAcwb'
    }

    # 定义请求函数
    def send_request(url, method, headers, data=None):
        try:
            response = requests.request(url=url,method=method,headers=headers,data=payload)
            print(response.json())
            # 打印线程的执行情况
            thread_id = threading.get_ident()
            print(f"Thread {thread_id} - 请求成功: {response.text}")
        except requests.exceptions.RequestException as e:
            # 打印线程的执行情况
            thread_id = threading.get_ident()
            print(f"Thread {thread_id} - 请求出错: {e}")

    # 定义请求头部参数
    headers = {
        "User-Agent": "Your User Agent",
        "Content-Type": "application/json",
        # 添加其他自定义的头部参数
    }

    # 定义线程数
    num_threads = 1

    # 使用线程池进行并发请求
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        # 提交任务到线程池
        futures = []
        for _ in range(num_threads):
            futures.append(executor.submit(send_request, url, "GET", headers,payload))
            # 如果需要进行POST请求，可以使用下面这行代码
            # futures.append(executor.submit(send_request, url, "POST", headers, payload))

        # 等待所有任务完成
        concurrent.futures.wait(futures)
def testtiger():
    t111 = 0
    t222 =0
    t333 =0
    t444 = 0
    t555 =0
    t666 = 0
    twww = 0
    ssw = 0
    sws = 0
    wss = 0
    rww = 0
    wrw = 0
    wwr = 0
    m=1000
    for i in range(0,m):
        import requests

        url = "https://active-sandbox.lita.gg/act/slotMachine/letLottery?num=100"

        payload = {}
        headers = {
            'AccessToken': 'WeCg9mA1oJ/miq3ac3xZO0hnEMpzn1C8S9skxIGIwYsWY/WQLaT7HDagaBrmXAe8'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        if response.json()["status"] != "0":
            print(response.json())
        elif response.status_code != 200:
            print("服务器异常！")
        result = response.json()["data"]["lotteryResult"]
        result = response.json()["data"]["lotteryResult"]
        if result[0] == result[1] == result[2] == "0" and t111 == 0:
            t111 += 1
            print("t111的赔率是%s"%(response.json()["data"]["ratio"]))
        elif result[0] == result[1] == result[2] == "1" and t222 == 0:
            t222 += 1
            print("t222的赔率是%s"%(response.json()["data"]["ratio"]))
        elif result[0] == result[1] == result[2] == "2" and t333 == 0:
            t333 += 1
            print("t333的赔率是%s"%(response.json()["data"]["ratio"]))
        elif result[0] == result[1] == result[2] == "3" and t444 == 0:
            t444 += 1
            print("t444的赔率是%s"%(response.json()["data"]["ratio"]))
        elif result[0] == result[1] == result[2] == "4" and t555 == 0:
            t555 += 1
            print("t555的赔率是%s"%(response.json()["data"]["ratio"]))
        elif result[0] == result[1] == result[2] == "5" and t666 == 0:
            t666 += 1
            print("t666的赔率是%s"%(response.json()["data"]["ratio"]))
        elif result[0] == result[1] == result[2] == "6" and twww == 0:
            twww += 1
            print("twww的赔率是%s"%(response.json()["data"]["ratio"]))
        elif result[0] == result[1] and result[2] == "6" and ssw == 0:
            ssw += 1
            print("ssw的赔率是%s"%(response.json()["data"]["ratio"]))
        elif result[0] == result[2] and result[1] == "6" and sws == 0:
            sws += 1
            print("sws的赔率是%s"%(response.json()["data"]["ratio"]))
        elif result[0] == "6" and result[1] == result[2] and wss == 0:
            wss += 1
            print("wss的赔率是%s"%(response.json()["data"]["ratio"]))
        elif result[1] == result[2] == "6" and rww == 0:
            rww += 1
            print("rww的赔率是%s"%(response.json()["data"]["ratio"]))
        elif result[0] == result[2] == "6" and wrw == 0:
            wrw += 1
            print("wrw的赔率是%s"%(response.json()["data"]["ratio"]))
        elif result[0] == result[1] == "6" and wwr == 0:
            wwr += 1
            print("wwr的赔率是%s"%(response.json()["data"]["ratio"]))
        elif t111 == t222 == t333 == t444 == t555 == t666 == twww == ssw == sws == wss == rww == wrw == wwr == 1:
            print("测试结束！")
            break
def teststar():
    for r in [30,70,300,1000]:
        s=0
        t=0
        m=100
        for i in range(0,m):
            import requests

            url = "https://active-sandbox.lita.gg/act/slotMachine/letLottery?num="+str(r)

            payload = {}
            headers = {
                'AccessToken': 'ritfHH5oGNL0649XkYJct8ge2w7MJCKnAj3ymVO0XCyL3JP+53gCRLzGROlrgNJs'
            }

            response = requests.request("GET", url, headers=headers, data=payload)
            #print(response.json())
            if response.json()["status"] != "0":
                print(response.json())
            elif response.status_code != 200:
                print("服务器异常！")
            result = response.json()["data"]
            if result["seaShellNum"] != "0":
                s += 1
            if result["ratio"] != "0":
                t += 1
        print("下注%s珍珠，星星中奖概率：%s"%(r,s/(m-t)))
def testlottery():
    l = 0
    coin = 0
    getcoin = 0
    m = 10000
    for i in range(0, m):
        import requests

        url = "https://active-sandbox.lita.gg/act/slotMachine/letLottery?num=300"

        payload = {}
        headers = {
            'AccessToken': 'u/CKsSa3VMhXEXYGt4VeZVp/8jXtZ3Qtvwf7bnppZEHpKjeTBE5uhTuR3owX24Ao'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        if response.json()["status"] != "0":
            print(response.json())
            print("循环次数是%s" % (m))
            break
        if response.status_code != 200:
            print("循环次数是%s" % (m))
            break
        result = response.json()["data"]
        if result["pearlNum"] != "0":
            l += 1
            getcoin += int(result["pearlNum"])
            print("%s次中奖次数是%s"%(i,l))
        coin += 300


    print("返奖率：%s"%(l/m))
    print("总花费是：%s,总获得是：%s"%(coin,getcoin))






if __name__ == '__main__':
    #testboxinvip()
    #testsvipbox()
    #testboxnotvip()
    buygiftpack()
    #activelottery()
    #testmany()
    #testtiger()
    #teststar()
    #testlottery()