import json

import urllib3
from urllib import request
def post_request():
    url = "http://httpbin.org/get"
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

    req = request.Request(url=url, headers=headers) # 传递的Request对象
    print(req)
    res = request.urlopen(req)
    print(res.read().decode())
def get_token():
    import requests
    url = "http://api-test.funbit.me/funbit/v2/player/recommend/batch?page=1&rows=10&batchNo="
    pyload = {}
    header  = {
        "AccessToken":"u/CKsSa3VMhXEXYGt4VeZWe56gmIW/QIUI8Ln/EoIFxiYVsN31f/agXihN4LIZHO"

    }
    rsp = requests.request(method="GET",url=url,data=pyload,headers=header)
    #rspdata = json.loads(rsp.json())
    #jsondata = json.dumps(rspdata,indent=2)
    responseData = rsp.json()
    print(rsp.status_code)
    #print(json.dumps(rsp.json(),indent=4))
    user = responseData["data"]["rows"][0]
    print(json.dumps(user,indent=4))
if __name__ == '__main__':
    get_token()