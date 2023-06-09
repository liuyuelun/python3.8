
import requests,time,json,threading
from datetime import datetime
jinbi = 0
zhongji =0
gaoji = 0
chujimai = 0
zhongjimai = 0
gaojimai = 0
qipao = 0
m = 100
t = 100
start_time = datetime.now()
print(start_time)
def draw():
    import requests
    import json

    url = "https://api-test.funbit.me/litaroom/giftpack/lottery/draw"

    payload = json.dumps({
        "roomId": "2000",
        "times": "1"
    })
    headers = {
        'Content-Type': 'application/json',
        'AccessToken': 'ritfHH5oGNL0649XkYJct3HO6nvNkbzNT21PftGAsgvNc9jk1zTSk3lrzdyL8Xsd'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response
def gogogo():
    global m,jinbi,zhongji,gaoji,chujimai,zhongjimai,gaojimai,qipao
    for i in range(1,m):
        time.sleep(3)
        response = draw()
        if response.status_code != 200:
            print("接口异常,状态码是：%s"%(response.status_code))
            break
        elif response.json()["status"] != "0":
            print(response.json())
            break
        else:
            name = response.json()["data"]["results"][0]["name"]
            id = response.json()["data"]["results"][0]["id"]
            if id == '1':
                #name == "现金800块":
                jinbi += 1
                print("总抽奖次数：%s,抽中%s的次数是：%s"%(m*t,name,jinbi))
            elif id == '2':
                #name == "高级礼物":
                gaoji += 1
                print("总抽奖次数：%s,抽中%s的次数是：%s"%(m*t,name,gaoji))
            elif id == '3':
                #name == "中级礼物":
                zhongji += 1
                print("总抽奖次数：%s,抽中%s的次数是：%s" % (m*t, name, zhongji))
            elif id == "4":
                    #name == "VVIP——麦位框" or name == "圣诞麦位头像框" or name == "总裁麦位框":
                chujimai += 1
                print("总抽奖次数：%s,抽中%s的次数是：%s" % (m*t, name, chujimai))
            elif id == "5":
                #name == "彩灯麦位框" or name == "idol活动奖励_No.1"or name == "idol活动奖励_No.2":
                zhongjimai += 1
                print("总抽奖次数：%s,抽中%s的次数是：%s" % (m*t, name, zhongjimai))
            elif id == "6":
                #name == "idol活动奖励_No.3" or name == "牛油果家族麦位框"or name == "情人节活动奖励Top1":
                gaojimai += 1
                print("总抽奖次数：%s,抽中%s的次数是：%s" % (m*t, name, gaojimai))
            elif id == '7':
                #name == "聊天气泡":
                qipao += 1
                print("总抽奖次数：%s,抽中%s的次数是：%s" % (m*t, name, qipao))
def result():
    if jinbi != 0:
        print("金币的的抽中概率是%s" % (jinbi / (m * t)))
    else:
        print("未抽中金币")
    if zhongji != 0:
        print("中级礼物的抽中概率是%s" % (zhongji / (m * t)))
    else:
        print("未抽中中级礼物")
    if gaoji != 0:
        print("高级礼物的抽中概率是%s" % (gaoji / (m * t)))
    else:
        print("未抽中高级礼物")
    if chujimai != 0:
        print("初级麦位框的抽中概率是%s" % (chujimai / (m * t)))
    else:
        print("未抽中初级麦位框")
    if zhongjimai != 0:
        print("中级麦位框的抽中概率是%s" % (zhongjimai / (m * t)))
    else:
        print("未抽中中级麦位框")
    if gaojimai != 0:
        print("中级麦位框的抽中概率是%s" % (gaojimai / (m * t)))
    else:
        print("未抽中高级麦位框")
    if qipao != 0:
        print("气泡的抽中概率是%s" % (qipao / (m * t)))
    else:
        print("未抽中气泡")
def manynumber():
    threads = []
    for i in range(t):
        print('thread %s is running...%s'%(threading.current_thread().name,threading.current_thread().ident))
        t1 = threading.Thread(target=gogogo)
        t1.start()
        threads.append(t1)
    for t1 in threads:
        t1.join()
    result()
    end_time = datetime.now()
    print(end_time)
    print("脚本总耗时是%s"%(end_time-start_time))
if __name__ == '__main__':
    manynumber()
    #gogogo()
    #print(draw().json())
    #result()