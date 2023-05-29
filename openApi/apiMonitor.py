import requests
import json
import xlrd

class ApiTest:
    def __init__(self, file_name):
        self.file_name = file_name

    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        table = data.sheet_by_index(0)
        nrows = table.nrows
        result = []
        for i in range(1, nrows):
            row_values = table.row_values(i)
            result.append(row_values)
            print(result)
        return result

    def run(self):
        rows = self.get_data()
        for row in rows:
            method = row[0]
            url = row[1]
            params = row[2]
            headers = row[3]
            expect = row[4]
            pre_resp_value = row[5]
            pre_resp_key = row[6]

            # 处理参数和请求头
            if pre_resp_key and pre_resp_value:
                if isinstance(pre_resp_value, float):
                    pre_resp_value = int(pre_resp_value)
                if pre_resp_value.startswith("$"):
                    pre_resp_value = json.loads(pre_resp_value[1:])
                if pre_resp_key.startswith("$"):
                    pre_resp_key = json.loads(pre_resp_key[1:])
                if isinstance(pre_resp_key, list):
                    for i in range(len(pre_resp_key)):
                        if pre_resp_key[i] in pre_resp_value:
                            params = params.replace(pre_resp_key[i], str(pre_resp_value[pre_resp_key[i]]))
                            headers = headers.replace(pre_resp_key[i], str(pre_resp_value[pre_resp_key[i]]))
                else:
                    if pre_resp_key in pre_resp_value:
                        params = params.replace(pre_resp_key, str(pre_resp_value[pre_resp_key]))
                        headers = headers.replace(pre_resp_key, str(pre_resp_value[pre_resp_key]))

            # 发送请求
            if method.lower() == "get":
                resp = requests.get(url=url, params=params, headers=json.loads(headers))
            elif method.lower() == "post":
                resp = requests.post(url=url, data=params, headers=json.loads(headers))
            else:
                raise ValueError("Invalid method: {}".format(method))

            # 断言响应内容
            if expect in resp.text:
                print("Test Passed")
            else:
                print("Test Failed")

if __name__ == '__main__':
    api_test = ApiTest("api.xls")
    api_test.run()
