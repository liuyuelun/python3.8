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

if __name__ == '__main__':
    zhuanyi()