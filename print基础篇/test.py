# !encoding=utf-8
"""
    auth:chenhao
    date:2022/06/14
"""

import requests
import logging
import os.path
import traceback
import urllib3
from subprocess import getstatusoutput

logging.basicConfig(level=logging.INFO, filename=os.path.abspath(os.path.dirname(__file__)) + '/requests.log',
                    format='%(asctime)s - %(funcName)s{} -%(levelname)s : %(message)s'.format("方法"))


class Respones(object):
    """判断接口是否正常且重启的类"""
    urls = [
        'https://域名或IP/forestar-patrol-sthly-cs',
        'https://域名或IP/sthlyxxgl-cs',
        'https://域名或IP/geodbService-cs'
    ]
    sername = [
        '大数据应用系统',
        '人员信息管理系统',
        'geodb系统'
    ]

    def __init__(self):
        """初始化方法"""
        self.patrol_error = []
        self.xxgl_error = []
        self.geodb_error = []

    def restart(self, cmd, servicename):
        """重启服务的方法"""
        logging.warning("进入重启jar包的方法")
        res = getstatusoutput(cmd)
        res_stat = res[0]
        if res_stat == 0 or res_stat == -9:
            logging.info("{0}服务重启完毕！sys状态{1}".format(servicename, res_stat))
        else:
            logging.error("{0}服务重启失败，抛出异常！\n{1}".format(servicename, traceback.format_exc()))

    def request_service(self):
        """请求接口的方法"""
        for url, name in zip(self.urls, self.sername):
            urllib3.disable_warnings()
            http_get = requests.get(url, timeout=30, verify=False)
            http_code = http_get.status_code
            if http_code == 200:
                logging.info("{0}服务正常！返回状态码:{1}".format(name, http_code))
                if name == '大数据应用系统':
                    self.patrol_error.clear()
                elif name == '人员信息管理系统':
                    self.xxgl_error.clear()
                elif name == 'geodb系统':
                    self.geodb_error.clear()
            elif http_code == 301 or http_code == 302:
                logging.warning("{0}服务可能出现了问题，似乎对系统没有影响。返回状态码:{1}".format(name, http_code))
                if name == '大数据应用系统':
                    self.patrol_error.clear()
                elif name == '人员信息管理系统':
                    self.xxgl_error.clear()
                elif name == 'geodb系统':
                    self.geodb_error.clear()
            elif http_code == 400 or http_code == 403 or http_code == 404 or \
                    http_code == 500 or http_code == 502 or http_code == 503:
                logging.error("{0}服务异常！返回状态码:{1}".format(name, http_code))
                if name == '大数据应用系统':
                    self.patrol_error.append(http_code)
                elif name == '人员信息管理系统':
                    self.xxgl_error.append(http_code)
                elif name == 'geodb系统':
                    self.geodb_error.append(http_code)
            else:
                logging.warning("{0}服务返回了一个无效状态码，请确认！返回状态码:{1}".format(name, http_code))


if __name__ == '__main__':
    """主程序"""
    from time import sleep

    respones = Respones()
    while True:
        respones.request_service()
        logging.warning("大数据应用系统错误码：{}".format(respones.patrol_error))
        logging.warning("信息管理系统错误码：{}".format(respones.xxgl_error))
        logging.warning("geodb系统错误码：{}".format(respones.geodb_error))
        if len(respones.patrol_error) >= 3:
            logging.info("大数据应用系统执行重启方法")
            respones.restart('cd /data/jl/service-18086-forestar-patrol-web && ./restart.sh', '大数据应用系统')
            respones.patrol_error.clear()
        elif len(respones.xxgl_error) >= 3:
            logging.info("人员信息管理系统执行重启方法")
            respones.restart('cd /data/jl/service-9334-sthlyxxgl && ./restart.sh', '人员信息管理系统')
            respones.xxgl_error.clear()
        elif len(respones.geodb_error) >= 3:
            logging.info("geodb系统执行重启方法")
            respones.restart('cd /data/jl/Tomcat-9001-geodbService && ./restart.sh', 'geodb系统')
            respones.geodb_error.clear()
        sleep(60)
