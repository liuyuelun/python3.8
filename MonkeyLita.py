import os

def monkeytest():
    adbmonkey =(
                "adb shell monkey -p com.funbit.android"
               " -s 6688 --throttle 100 --pct-touch 50"
               " --pct-motion 50 --ignore-crashes --ignore-timeouts"
               " --monitor-native-crashes -v-v-v 1000 > ./monkey/run.log"
            )
    adbtest = (
        "adb shell monkey -p com.funbit.android"
        " -s 6688 --ignore-timeouts --throttle 500 "
        "--monitor-native-crashes -v-v-v 1000 > ./monkey/run.log"
    )
    adbstart = "source ~/.bash_profile"
    javasource = "java -jar monkeyTest.jar"
    os.system("%s && %s && %s"%(adbstart,adbtest,javasource))
    #os.system("%s && %s"%(adbstart,adbtest))

if __name__ == '__main__':
    monkeytest()