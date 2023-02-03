#数据组织结构

def if_else():
    num = int(input("请输入一个整数：\n"))
    if num/2 == 0:
        print(num,"是偶数")
    else:
        print(num,"是奇数")

def if_elif():
    score = int(input("请输入您的分数:\n"))
    if  90 <= score <=100:
        print("成绩A级")
    elif 80 <= score <=90:
        print("成绩B级")
    elif 60 <= score <=70:
        print("成绩C级")
    else:
        print("成绩不及格")

def if_in_if():
    """
    会员消费金额>=200:8折
    会员消费金额>=100：9折
    会员消费<100：不打折

    不是会员消费>=200：9.5折
    不是会员<200：不打折
    :return:
    """
    ansewer = input("您是会员吗（y/n）？\n")
    money = int(input("请输入您的消费金额：\n"))
    if ansewer == "y":
        if money >= 200:
            print("您最终消费金额为：",money*0.8)
        elif 100 <= money <=200:
            print("您最终消费金额为：",money*0.9)
        else:
            print("您的最终消费金额：",money)
    else:
        if money >= 200:
            print("您的最终消费为：",money*0.95)
        else:
            print("您的最终消费为：",money)

if __name__ == '__main__':
    if_in_if()