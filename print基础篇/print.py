#print函数
def prt():
    """
    1、print（）可以输出哪些内容？
        print（）可以输出数字
        print（）可以输出字符串（引号）
        print（）可以输出含有运算符的表达式
    2、print（）函数可以将内容输出的目的地？
        显示器
        文件
    3、print函数的输出形式？
        换行
        不换行
    """
    #print（）可以输出数字
    print(99)
    print(99.99)

    #print（）可以输出字符串（单双引号）
    print("hello world")

    #print（）可以输出含有运算符的表达式
    print(3+1)

    #将使数据输出到文件:
    #1、输出的文件路径真实存在
    #2、print需要追加file=文件
    fp = open("./test.txt","a+")  #a+文件不存在创建文件，不存在追加内容
    print("hello world",file=fp)
    fp.close()

    #不进行换行输出：使用 ，分割内容
    print("Lily","Tom","Jack")

#转义字符与原字符
def zhuanyi():
    """
    1、什么时转义字符？
        就是反斜杠+想要实现转义功能的首字符
    2、为什么需要转义字符？
        当字符串中包含反斜杠、单引号、双引号等有特殊用途的字母时，必须使用反斜杠对这些字符串进行转义
            反斜杠：\\
            单引号：\'
            双引号：\"
        当字符串中包含换行、回车、水平制表符或退格等无法直接表示的特殊字符时，也可以使用转义字符当字符串：
            换行：\n   new line    换行
            回车：\r   return    回到当行首位
            水平制表符：\t   table  \t四个字符位
            退格：\b    back     回退覆盖一个字符
    3、转义字符：不希望字符串中的转义字符起作用，在原字符串之前加一个r或R
        注意事项：最后一个字符串不能是饭斜杠
    :return:
    """
    print("http:\\\\baidu.com","转义反斜杠")
    print("\'转义单引号\'")
    print("\"转义双引号\"""")
    print("hello\nworld","换行符")
    print("hello\tworld","制表符：一个制表符占四个字符")
    print("helloooo\tworld","制表符：一个制表符占四个字符,不足四个补足剩余")
    print("hello\rworld","world覆盖hello")
    print("hello\bworld","回退一格覆盖掉o")
    print(r"hello\nworld","小写r的原字符")
    print(R"hello\nworld","大写R的原字符")

#二进制与字符编码
def bianma():
    print(chr(0b10001010001))
    print(ord("中"))

#标识符与保留字
def biaoshifu():
    """
    1、我的保留字：
        有一些单词被我赋予了特定的意义，这些单词在给你任意对象起名字的时候都不可以使用
    2、我的规则你必须知道：
        变量、函数、类、模块、和其他对象起的名字就叫标识符
        规则：
            字母、数字、下划线
            不能以数字开头
            不能是我的保留字
            严格区分大小写
    :return:
    """
    import keyword
    print(keyword.kwlist)

#变量的定义和使用
def variable_use():
    """
    变量有三部分组成：
        1、标识：标识对象所存储的内存地址，使用内置函数id(obj)来获取
        2、类型：表示的是对象的数据类型，使用内置函数type(obj)来获取
        3、值：表示对象所存储的具体数据，使用print()obj可以将值打印输出
    :return:
    """
    name = "马丽亚"
    name0 = "汤姆"
    print("变量name的内存地址是：%s"%(id(name)))
    print("变量name的数据类型是%s"%(type(name)))
    print("变量name的值是：%s"%(name))
    name = name0
    print("变量name的内存地址是：%s"%(id(name)))
    print("变量name的数据类型是%s"%(type(name)))
    print("变量name的值是：%s"%(name))
    #name = "杰克"

#数据类型
def data_type():
    """
    常见的数据类型：
        整数类型：int，98
            英文为integer，简写int，可以表示正数、负数和零
        浮点类型：float，3.1415926
            浮点类型由浮点整数部分和浮点小数部分组成
            使用浮点数进行计算时，可能出现小数位数不确定的情况
        布尔类型：bool，true
            可以转成整数计算，true表示1，false表示0
        字符串类型：str，"人生苦短，我用python"
            字符串又被称为不可变的字符序列
            可以使用单引号''、双引号""、三单引号''' '''、三双引号""" """表示
            单引号或双引号定义的字符串，必须在一行
            三引号表示的字符串，可以分布在连续的多行
    :return:
    """
    #整数类型：二进制（0b开头）、十进制、八进制（0o开头）、十六进制（0x开头）
    print("==============================整数=========================")
    print("二进制\t","0b10101111\t",0b10101111)
    print("十进制\t","888\t",888)
    print("八进制\t","0o176\t",0o176)
    print("十六进制\t","0x12345\t",0x12345)

    #浮点型：导入decimal解决计算不准确的问题
    print("==============================小数=========================")
    n1 = 1.1
    n2 = 2.2
    print(n1+n2)
    from decimal import Decimal
    print(Decimal("1.1")+Decimal("2.2"))

    #布尔类型可以转成整数来计算
    print("==============================布尔类型=========================")
    f1 = True
    f2 = False
    print(f1+1)
    print(f2+1)

    #字符串类型
    print("==============================字符串类型=========================")
    str1 = "人生苦短，我用python"
    str2 = """
            人生苦短
            我用python
            """
    print(str1,type(str1))
    print(str2,type(str2))

#类型转换
def type_change():
    """
    str() : 将其他类型转换成字符串，也可用引号
    int() : 将其他类型转换成整数：
                文字类和小数类无法转换成整型
                浮点型转成整型，抹零取整
    _float() : 将其他类型转换成浮点数：
                文字类无法转换成整数
                整数转换为浮点型，末尾带.0
    :return:
    """
    name = "张三"
    age = 18
    print(type(name),type(age))
    print("我叫"+name+"今年"+str(age))

    a = 10
    b = 98.8
    c=True
    print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))

    m = "99"
    n = 9.9
    l = "19.9"
    print(type(m),type(n),type(l),type(int(m)),type(int(n)),type(int(float(l))))


if __name__ == '__main__':
    type_change()