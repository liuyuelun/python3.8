import requests
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

if __name__ == '__main__':
    draw()