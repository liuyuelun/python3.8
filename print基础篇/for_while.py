def while_sum():
    num = 0
    s = 0
    while num < 101:
        num += 2
        s += num
        print(s)
    print(s)
    return s

def for_num():
    for i in range(100, 1000):
        ge = i % 10
        shi = i // 10 % 10
        bai = i // 100
        # print(bai,shi,ge)
        num = ge ** 3 + shi ** 3 + bai ** 3
        if num == i:
            print(i, "是水仙花数")

def for_breake():
    pwd = input("请输入密码：\n")
    for item in range(3):
        if pwd == "8888":
            print("密码正确")
            break
        else:
            print("密码错误")
            pwd = input("请重新输入密码：\n")

def for_continue():
    """
    要求输出1~50，不是5倍数的所有数，，要求使用continue实现
    :return:
    """
    for item in range(51):
        if item % 5 == 0:
            continue
        else:
            print(item)

def for_else():
    pwd = input("请输入密码：\n")
    for item in range(2):
        if pwd == "8888":
            print("密码正确")
            break
        else:
            pwd = input("密码错误,请重新输入：\n")
    else:
        print("密码已输入错误三次，请明天再试")

def for_in_for():
    for i in range(1,10):
        for j in range(1,i+1):
            print(str(i)+"x"+str(j)+"="+str(i*j),end="\t")
        print()





if __name__ == '__main__':
    for_in_for()
