import requests
import json

class HTTPRequest:
    def __init__(self):
        self.session = requests.Session()

    def request(self, method, url, **kwargs):
        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            return response.content
        except requests.exceptions.RequestException as e:
            print(f'Request failed: {e}')
            return None

    def get(self, url, params=None, **kwargs):
        return self.request('GET', url, params=params, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.request('POST', url, data=data, json=json, **kwargs)
hr = HTTPRequest()

# 发送GET请求
response = hr.get('https://jsonplaceholder.typicode.com/todos/1')
print(response)

# 发送POST请求
response = hr.post('https://jsonplaceholder.typicode.com/posts', json={'title': 'foo', 'body': 'bar', 'userId': 1})
print(response)
