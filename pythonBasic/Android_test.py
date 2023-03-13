# -*- coding: utf-8 -*-
import os
import time

from ui2 import send_gift
import csv

"""class startSession(object):
    def __init__(self,desired_caps):
        self.desired_caps = desired_caps

    def run(self):
        print('******* StartSession ******')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        return self.driver

    def desired_caps(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.1'
        desired_caps['automationName'] = "uiautomator2"
        desired_caps['deviceName'] = '2f7e2ac9'  # YDBUJNYL8SNNPZGE   2f7e2ac9
        desired_caps['noReset'] = 'true'
        desired_caps['appActivity'] = 'com.oppopay.payments.ui.activity.SplashActivity'
        desired_caps['androidDeviceReadyTimeout'] = '180'
        desired_caps['appPackage'] = 'com.oppopay.payments'
        return desired_caps
    def start_app(self):
        driver = startSession(self.desired_caps()).run()  #"""

def memory_test():
    """
    采用adb shell dumpsys meminfo命令后面加apk包名来检查此app的内存消耗情况
    native：Native代码分配的内存，虚拟机和Android框架分配内存。
            关于什么是Native代码，即非Java代码分配的内存
    dalvik：Java对象分配的占据内存
    :return:
    """
    alldata = [("native", "dalvik", "TOTAL","Activities","views")]  # 写到表格中三个字段
    # 设置循环次数
    count = 100  # 设置获取内存占用的次数
    while count > 0:
        send_gift()
        lines = os.popen(". ~/.bash_profile;adb shell dumpsys meminfo com.funbit.android")  # adb 查看app内存
        result = lines.read()
        # 以逗号分隔
        temp = ','.join(result.split())

        native_heap = temp.split('Native,Heap')[1].split(',')[1]
        print("native_heap:" + str(native_heap))

        dalvik_heap = temp.split('Dalvik,Heap')[1].split(',')[1]
        print("dalvik_heap:" + str(dalvik_heap))

        total = temp.split('TOTAL')[1].split(',')[1]
        print("total:" + str(total))

        activities = temp.split('Activities')[1].split(',')[1]
        print("Activities:" + str(activities))

        Views = temp.split('Views')[1].split(',')[1]
        print("Views:" + str(Views))

        alldata.append([native_heap, dalvik_heap, total,activities,Views])
        count -= 1
        print('还剩余：%s次' % count)
        time.sleep(5)  # 等待时间
        # 将打印结果写到文件中。
        file = open('test.csv', 'w')
        writer = csv.writer(file)
        writer.writerows(alldata)
        file.close()


def test_popen():
    f = os.popen("ls")
    #l = f.readlines()
    #read = f.read()
    #print(read)
    #readline = f.readline()
    #print(readline)
    readlines = f.readlines()
    print(readlines)



if __name__ == '__main__':
    memory_test()