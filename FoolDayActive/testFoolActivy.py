# -*- coding:utf-8 -*-#
import requests
import json
host = "https://active-sandbox.lita.gg"
def get_active():
    for i in range(0,2):
        apigetavtice = "/active/aprilFoolsDayAct/panel"
        AccessToken = ["","u/CKsSa3VMhXEXYGt4VeZZM/S20lvAILKu1x3L5/D6i/OPhcdmpA+3A0L3P698Hl"]
        url = host+apigetavtice
        pyload = {}
        headers = {
            "Content-Type":"application/json",
            "charset":"utf-8",
            "AccessToken":AccessToken[i]
        }
        res = requests.request("GET",url=url,headers=headers,data=pyload)#.encoding = "utf-8"
        if i == 0:
            print("============================================================================")
            print("未登录进入活动页：\n{0}".format(json.dumps(res.json(encoding="utf-8"),indent=4,ensure_ascii=False)))
        if i == 1:
            print("============================================================================")
            print("登录进入活动页：\n{0}".format(json.dumps(res.json(),indent=4,sort_keys=True)))

def buy_GiftPack():
    for i in range(0,3):
        apigetavtice = "/active/aprilFoolsDayAct/buyGiftPack"
        AccessToken = ["","u/CKsSa3VMhXEXYGt4VeZZM/S20lvAILKu1x3L5/D6i/OPhcdmpA+3A0L3P698Hl","RcRp8XIl1sKi0nwE1qK3uK00zf8q7pgCN7K9+qnIfX95n9Y1CiBjDkI9p/ymuse4"]
        url = host+apigetavtice
        pyload = {}
        headers = {
            "Content-Type":"application/json",
            "charset":"utf-8",
            "AccessToken":AccessToken[i],
        }
        res = requests.request("GET",url=url,headers=headers,data=pyload)#.encoding = "utf-8"
        if i == 0:
            print("============================================================================")
            print("未登录购买礼包：\n{0}".format(json.dumps(res.json(encoding="utf-8"),indent=4,ensure_ascii=False)))
        if i == 1:
            print("============================================================================")
            print("登录购买礼包：\n{0}".format(json.dumps(res.json(),indent=4,sort_keys=True,ensure_ascii=False)))
        if i == 2:
            print("============================================================================")
            print("余额不足购买礼包：\n{0}".format(json.dumps(res.json(),indent=4,sort_keys=True,ensure_ascii=False)))

def juggle():
    for i in range(0,3):
        AccessToken = ["","u/CKsSa3VMhXEXYGt4VeZZM/S20lvAILKu1x3L5/D6i/OPhcdmpA+3A0L3P698Hl","RcRp8XIl1sKi0nwE1qK3uK00zf8q7pgCN7K9+qnIfX95n9Y1CiBjDkI9p/ymuse4"]
        count = ["",0,-1,1,10,100,"str","1"]
        pyload = {
        }
        headers = {
            "Content-Type":"application/json",
            "charset":"utf-8",
            "AccessToken":AccessToken[i]
        }
        if i == 0:
            apigetavtice = "/active/aprilFoolsDayAct/juggle?count=10"
            url = host + apigetavtice
            res = requests.request("GET", url=url, headers=headers, data=pyload)
            print("============================================================================")
            print("未登录开启魔法帽：\n{0}".format(json.dumps(res.json(encoding="utf-8"),indent=4,ensure_ascii=False)))
        if i == 1:
            for n in range(0,8):
                apigetavtice = "/active/aprilFoolsDayAct/juggle?count=%s"%count[n]
                url = host + apigetavtice
                res = requests.request("GET", url=url, headers=headers, data=pyload)
                rsp = json.dumps(res.json(),indent=4,sort_keys=True,ensure_ascii=False)
                print("============================================================================")
                print("抽取次数count为：{0}，类型是{1}时，开启魔法帽:\n{2}".format(count[n],type(count[n]),rsp))
        if i == 2:
            apigetavtice = "/active/aprilFoolsDayAct/juggle"
            url = host+apigetavtice
            res = requests.request("GET",url=url,headers=headers,data=pyload)
            rsp = json.dumps(res.json(),indent=4,ensure_ascii=False)
            print("============================================================================")
            print("开启魔法帽时，未传入count参数时:\n{0}".format(rsp))

def fool_day_rank():
    for n in range(0,9):
        apigetactive = "/active/aprilFoolsDayAct/getYuleDayRanks?type=%s"%n
        url = host+apigetactive
        AccessToken = ["u/CKsSa3VMhXEXYGt4VeZZM/S20lvAILKu1x3L5/D6i/OPhcdmpA+3A0L3P698Hl",
                       "RcRp8XIl1sKi0nwE1qK3uK00zf8q7pgCN7K9+qnIfX95n9Y1CiBjDkI9p/ymuse4"]
        pyload = {}
        headers = {
            "Content-Type": "application/json",
            "charset": "utf-8",
            "AccessToken": AccessToken[0]
        }
        res = requests.request("GET",url=url,headers=headers,data=pyload)
        rsp = json.dumps(res.json(),indent=4,ensure_ascii=False)
        print("============================================================================")
        print("第{0}天愚人节日榜：\n{1}".format(n,rsp))
def all_rank():
    apigetactive = "/active/aprilFoolsDayAct/getYuleAllRanks"
    url = host + apigetactive
    AccessToken = ["u/CKsSa3VMhXEXYGt4VeZZM/S20lvAILKu1x3L5/D6i/OPhcdmpA+3A0L3P698Hl",
                   "RcRp8XIl1sKi0nwE1qK3uK00zf8q7pgCN7K9+qnIfX95n9Y1CiBjDkI9p/ymuse4"]
    pyload = {}
    headers = {
        "Content-Type": "application/json",
        "charset": "utf-8",
        "AccessToken": AccessToken[0]
    }
    res = requests.request("GET", url=url, headers=headers, data=pyload)
    rsp = json.dumps(res.json(), indent=4, ensure_ascii=False)
    print("============================================================================")
    print("愚人节总榜：\n{0}".format(rsp))

if __name__ == '__main__':
    #get_active()
    buy_GiftPack()
    #juggle()
    #fool_day_rank()
    #all_rank()