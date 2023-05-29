from locust import HttpUser, between, task
from locust import events
from getToken import token
import requests
class MyUser(HttpUser):
    """
    运行脚本：locust -f <Locust文件路径>
    查看性能监控：http://localhost:8089
    """
    wait_time = between(1, 5)

    @task(10)
    def getVoiceroom(self):
        header = {
            "authorization":token,
            "apptype":"android"
        }
        url = "/timo/room/recommend/getRecommendList?next=&findMode=any&roomType=all"
        print(url)
        self.client.get(url=url,headers=header)
        #events.request.fire(request_type="GET", name="首页语音房列表",ç
        #                            response_time=rsp.elapsed.total_seconds(), response_length=len(rsp.json()))

    @task(10)
    def roomlist(self):
        header = {
            "authorization": token
        }
        url = "/timo/basic/family/square/list?type=hotSquare&batchNo=-1&nextIndex=0&len=20"
        print(url)
        self.client.get(url=url, headers=header)

"""     
    @task
    def view_item(self):
        for item_id in range(10):
            self.client.get(f"/item?id={item_id}", name="/item")
    @task
    def on_start(self):
        data = {}
        header = {
            "AccessToken":"u/CKsSa3VMhXEXYGt4VeZene7PWte9HuWr+gwMH0eXAofcviuIeV8HQbVj/T6pSQ"
        }
        self.client.post("/login", json={"username":"foo", "password":"bar"})
"""