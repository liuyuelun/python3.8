# -*- coding: utf-8 -*-
import os
import time

#from appium import webdriver
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
    alldata = [("native", "dalvik", "TOTAL","Activities")]  # 写到表格中三个字段
    # 设置循环次数
    count = 20  # 设置获取内存占用的次数
    while count > 0:
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

        alldata.append([native_heap, dalvik_heap, total,activities])
        count -= 1
        print('还剩余：%s次' % count)
        time.sleep(5)  # 等待时间
        # 将打印结果写到文件中。
        file = open('test.csv', 'w')
        writer = csv.writer(file)
        writer.writerows(alldata)
        file.close()

def android_memory_test():
    native_heap = []
    dalvik_heap = []
    activities = []
    while True:
        cmd = ". ~/.bash_profile;adb shell dumpsys meminfo com.funbit.android>android.txt"
        os.system(cmd)
        f = open("android.txt","r")
        lines = f.readlines()
        for line in lines:
            if "Native Heap" in line:
                s=line.split()[2]
                native_heap.append(s)
            if "Dalvik Heap" in line:
                s=line.split()[2]
                dalvik_heap.append(s)
            if "Activities" in line:
                s = line.split()[1]
                activities.append(s)
        time.sleep(5)
        print(native_heap,dalvik_heap,activities)
        #return native_heap,dalvik_heap,activities

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
    #android_memory_test()
    #memory_test()
    test_popen()