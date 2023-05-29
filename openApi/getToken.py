import requests
class GetToken():
    def gettoken(self,id):
        self.id = str(id)
        url = "https://api-test.timo.team/timo/basic/login/fuckToken?userId="+self.id
        headers = {
            "whosyourdaddy": "fuckToken123456789qwertyuiopasdfghjklzxcvbnm"
        }
        rsp = requests.get(url=url,headers=headers)
        token = rsp.json()["data"]["accessToken"]
        print("=======================================================================")
        return token
token = GetToken().gettoken(19)

print(token)