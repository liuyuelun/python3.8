import os

get_lancher_activity = "adb shell dumpsys activity activities | grep 'mCurrentFocus'"
lancher_activity = "com.funbit.android/.ui.splash.SplashActivity"
kill_app = "adb shell  am force-stop com.funbit.android"

lita = "adb shell am start -W -S -R 10 com.funbit.android/.ui.splash.SplashActivity>./log/lita.log"
yalla = "adb shell am start -W -S -R 10 com.weieyu.yalla/com.yalla.yalla.main.ui.activity.StartActivity>./log/yalla.log"
partying = "adb shell am start -W -S -R 10 com.imbb.oversea.android/com.imbb.banban.android.MainActivity>./log/partying.log"
cocofun = "adb shell am start -W -S -R 10 com.icocofun.us.maga/.SplashActivity>./log/cocofun.log"
hago = "adb shell am start -W -S -R 10 com.yy.hiyo/.MainActivity>./log/hago.log"
bixin = "adb shell am start -W -S -R 10 com.yitantech.gaigai/com.bx.splash.SplashActivity>./log/bixin.log"

def starttime(app):
    stop_app = app.split("/")[0].split(" ")[-1]
    tobestop = "adb shell am force-stop " + stop_app
    source_bash = "source ~/.bash_profile"
    print(tobestop)
    os.system("%s && %s && %s"%(source_bash,app,tobestop))
    log = app.split(">")[1]
    with open(log,"r") as log_ft:
        number = 0
        TotalTime = 0
        totaltime = 0
        for line in log_ft.readlines():
            if "TotalTime" in line:
                totaltime = int(line.split(":")[1])
                number = number + 1
                TotalTime = totaltime + TotalTime
        new_app = app.split(">")[1].split(".")[0]
        AvgTime = new_app+"冷启动10次的平均冷启时长为：" + str(TotalTime/number) + "ms"
    return AvgTime

if __name__ == '__main__':
    print(starttime(lita))
    print(starttime(yalla))
    print(starttime(partying))
    print(starttime(cocofun))
    print(starttime(hago))
    print(starttime(bixin))