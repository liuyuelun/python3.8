import time, threading
from datetime import datetime
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
m = 10
t=100
count = 1
global altime
alltime = m * count
start_time = datetime.now()
print(start_time)
def testboxinvip():

    global g6044,g6046,g6047,g6049,g6771,g6050,g6051,g6052,g6153,g6154,m

    count = 1
    global altime
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
            'AccessToken': 'WeCg9mA1oJ/miq3ac3xZO/48Z+maB8IKqfpa2Pfu5AryuL4R8j4cwAaoT8Lzq62H',
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
            break
        elif response.status_code != 200 :
            print("接口异常，状态码是%s"%(response.status_code))
            break
        else:
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
        print("宝箱中礼物g6044(%s)的概率是%s"%(g6044,g6044/(alltime*t)))
    else:
        print("未抽中g6044")
    if g6046 != 0:
        print("宝箱中礼物g6046(%s)的概率是%s"%(g6046,g6046/(alltime*t)))
    else:
        print("未抽中g6046")
    if g6047 != 0:
        print("宝箱中礼物g6047(%s)的概率是%s" % (g6047,g6047/(alltime*t)))
    else:
        print("未抽中g6047")
    if g6049 != 0:
        print("宝箱中礼物g6049(%s)的概率是%s" % (g6049,g6049/(alltime*t)))
    else:
        print("未抽中g6049")
    if g6771 != 0:
        print("宝箱中礼物g6771(%s)的概率是%s" % (g6771,g6771/(alltime*t)))
    else:
        print("未抽中g6771")
    if g6050 != 0:
        print("宝箱中礼物g6050(%s)的概率是%s" % (g6050,g6050 / (alltime*t)))
    else:
        print("未抽中g6050")
    if g6051 != 0:
        print("宝箱中礼物g6051(%s)的概率是%s" % (g6051,g6051 / (alltime*t)))
    else:
        print("未抽中g6051")
    if g6052 != 0:
        print("宝箱中礼物g6052(%s)的概率是%s" % (g6052,g6052 / (alltime*t)))
    else:
        print("未抽中g6052")
    if g6153 != 0:
        print("宝箱中礼物g6153(%s)的概率是%s" % (g6153,g6153 / (alltime*t)))
    else:
        print("未抽中g6153")
    if g6154 != 0:
        print("宝箱中礼物g6154(%s)的概率是%s" % (g6154,g6154 / (alltime*t)))
    else:
        print("未抽中g6154")

def openbox():
    import requests
    import json
    global count
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
        'AccessToken': 'WeCg9mA1oJ/miq3ac3xZO/48Z+maB8IKqfpa2Pfu5AryuL4R8j4cwAaoT8Lzq62H',
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
    return response
def testapi():
    global g6044,g6046,g6047,g6049,g6771,g6050,g6051,g6052,g6153,g6154,m
    for i in range(1,m+1):
        response = openbox()
        if response.json()["status"] != "0":
            print(response.json())
            break
        elif response.status_code != 200 :
            print("接口异常，状态码是%s"%(response.status_code))
            break
        else:
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
def result():
    if g6044 != 0:
        print("宝箱中礼物g6044(%s)的概率是%s" % (g6044, g6044 / (alltime * t)))
    else:
        print("未抽中g6044")
    if g6046 != 0:
        print("宝箱中礼物g6046(%s)的概率是%s" % (g6046, g6046 / (alltime * t)))
    else:
        print("未抽中g6046")
    if g6047 != 0:
        print("宝箱中礼物g6047(%s)的概率是%s" % (g6047, g6047 / (alltime * t)))
    else:
        print("未抽中g6047")
    if g6049 != 0:
        print("宝箱中礼物g6049(%s)的概率是%s" % (g6049, g6049 / (alltime * t)))
    else:
        print("未抽中g6049")
    if g6771 != 0:
        print("宝箱中礼物g6771(%s)的概率是%s" % (g6771, g6771 / (alltime * t)))
    else:
        print("未抽中g6771")
    if g6050 != 0:
        print("宝箱中礼物g6050(%s)的概率是%s" % (g6050, g6050 / (alltime * t)))
    else:
        print("未抽中g6050")
    if g6051 != 0:
        print("宝箱中礼物g6051(%s)的概率是%s" % (g6051, g6051 / (alltime * t)))
    else:
        print("未抽中g6051")
    if g6052 != 0:
        print("宝箱中礼物g6052(%s)的概率是%s" % (g6052, g6052 / (alltime * t)))
    else:
        print("未抽中g6052")
    if g6153 != 0:
        print("宝箱中礼物g6153(%s)的概率是%s" % (g6153, g6153 / (alltime * t)))
    else:
        print("未抽中g6153")
    if g6154 != 0:
        print("宝箱中礼物g6154(%s)的概率是%s" % (g6154, g6154 / (alltime * t)))
    else:
        print("未抽中g6154")

def manynumber():
    threads = []
    for i in range(t):
        print('thread %s is running...%s'%(threading.current_thread().name,threading.current_thread().ident))
        t1 = threading.Thread(target=testapi)
        t1.start()
        threads.append(t1)
    for t1 in threads:
        t1.join()
    result()
    end_time = datetime.now()
    print(end_time)
    print("脚本总耗时是%s"%(end_time-start_time))
