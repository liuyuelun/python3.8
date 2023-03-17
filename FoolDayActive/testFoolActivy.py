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
            "AccessToken":AccessToken[i]
        }
        res = requests.request("GET",url=url,headers=headers,data=pyload)
        if i == 0:
            print("============================================================================")
            print("未登录进入活动页：\n{0}".format(json.dumps(res.json(),indent=4,sort_keys=True)))
        if i == 1:
            print("============================================================================")
            print("登录进入活动页：\n{0}".format(json.dumps(res.json(),indent=4,sort_keys=True)))


if __name__ == '__main__':
    get_active()