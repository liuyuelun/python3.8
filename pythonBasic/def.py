def odd_event(t):
    odd = [] #存奇数
    even = []  #存偶数
    for i in t:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even

def args_tuple(*args):
    """
    多个位置参数，传入时按照元组传入
    :param args:
    :return:
    """
    for i in args:
        print(i)

def args_dict(**args):
    """
    多个键值对传入时，参数组合为字典传入
    :param args:
    :return:
    """
    print("**args的值是{0}：".format(args))
    print("args.items()的值是{0}：".format(args.items()))
    for k,v in args.items():
        print("参数：{0}\t 值：{1}".format(k,v))

def fac(n):
    """
    函数反复调用自身，直到终止
    递归组成部分：1、递归调用    2、终止条件
    :param n:
    :return:
    """
    if n == 1:
        return 1
    else:
        return n*fac(n-1)

def fib(n):
    """
    获取第n位的波菲那契数字
    :param n:
    :return:
    """
    if n ==1 :
        return 1
    elif n ==2 :
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fib_add(n):
    """
    获得n位的波菲那契数列
    :param n:
    :return:
    """
    res = ""
    for i in range(1,n+1):
         res +=str(fib(i))
    return int(res)

def division():
    try:
        a = int(input("请输入第一个整数：\n"))
        print(a)
        b = int(input("请输入第二个整数：\n"))
        print(b)
        result = a/b
        return result
    except ZeroDivisionError as e:
        print("被除数不能为0！")
        return division()
    except ValueError as e:
        print("请输入整数！")
        return division()
    except BaseException as e:
        print(e)
        return division()


if __name__ == '__main__':
    print(division())