def str_create():
    """字符串驻留机制
    仅保留一份相同的字符串
    """
    a = 'Python'
    b = "Python"
    c = """Python"""
    print("字符串a：%s"%a,id(a))
    print("字符串b：%s"%b,id(b))
    print("字符串c：%s"%c,id(c))
    d = "m".join(a)
    print("字符串d：%s"%d)

def str_find():
    d = "Pmymtmhmomn"
    """
    1、index(s)查找字符串中，s第一次出现的位置，如果不存在则抛出ValueError
    2、rindex(s)查找字符串中，s最后一次出现的位置，如果不存在则抛出ValueError
    3、find(s)查找字符串中，s第一次出现的位置，如果不存在则返回-1
    4、rfind(s)查找字符串中，s最后一次出现的位置，如果不存在则返回-1
    """
    print("字符串o在字符串%s第一次出现的位置：%s"%(d,d.index("m")))
    print("字符串o在字符串%s最后一次出现的位置：%s"%(d,d.rindex("m")))
    print("字符串o在字符串%s第一次出现的位置：%s"%(d,d.find("m")))
    print("字符串o在字符串%s第一次出现的位置：%s"%(d,d.rfind("m")))

def str_upper_lower():
    """
    s.upper()把字符串中所有字符创转换成大写
    s.lower()把字符创中所有字符串转换成小写
    s.swapcase()把字符串中所有大写转换成小写，所有小写转换成大写
    s.capitalize()把字符串第一个转换成大写，其余的转换成小写
    s.tittle()把字符串中每个单词首字符转换成大写，单词其余字母转换成小写
    :return:
    """
    s = "PythonISBest"
    print("把字符串%s都转换成大写后：%s"%(s,s.upper()))
    print("把字符串%s都转换成小写后：%s"%(s,s.lower()))
    print("把字符串%s大小写转换后：%s"%(s,s.swapcase()))
    print("把字符串%s第一个字符转换成大写，其余转成小写后：%s"%(s,s.capitalize()))
    print("把字符串%s每个单词首字符转换成大写，单词其余内容转换成小写后：%s"%(s,s.upper()))

def str_split():
    """
    s.split()：
        从字符串的左边开始劈分，默认劈分字符是空格，返回值均为一个列表
        通过参数sep指定劈分字符串
        通过参数maxsplit来指定最大劈分次数，达到最大劈分次数后，剩余字符串会单独作为一部分
    s.rsplit()：
        从字符串的右边开始劈分，默认劈分字符是空格，返回值均为一个列表
        通过参数sep指定劈分字符串
        通过参数maxsplit来指定最大劈分次数，达到最大劈分次数后，剩余字符串会单独作为一部分
    :return:
    """
    s = "hello world python"
    print("字符串%s按照空格从左侧劈分后：%s"%(s,s.split()))
    print("字符串%s按照'o'劈分一次后：%s"%(s,s.split(sep="o",maxsplit=1)))
    print("字符串%s按照空格从右侧劈分后：%s"%(s,s.rsplit()))
    print("字符串%s按照'o'从右侧劈分一次后：%s"%(s,s.rsplit(sep="o",maxsplit=1)))

def str_is():
    """
    s.isidentifier()判断字符串是不是合法标识符
    s.isspace()判断字符串是否全由空白字符串组成（空格、回车、制表符）
    s.isalpha()判断字符创是否全部由字母组成
    s.decimal()判断字符创是否全部由十进制组成
    s.isnumber()判断字符创是否全由数字组成
    s.isalnum()判断字符创是否全部由字母和数字组成
    :return:
    """
    s = "hello python 123"
    print("字符串%s是否全部由数字和字母组成：%s"%(s,s.isalnum()))

def str_replace():
    """
    reppace(n,m,num):第一个参数是被指定替换的字符串，第二个是替换指定字符串的内容，第三个参数是指定替换的最大次数
    join()：将列表或元组中的字符串合并成一个字符串
    :return:
    """
    s = "hello python python python"
    print(s.replace("python","java",1))
    l = ["python","java","go"]
    print("用拼接符|将列表%s的每个元素拼接成一个新字符串%s"%(l,"|".join(l)))
    print("用拼接符*将字符串%s的每个元素拼接成一个新字符串%s:"%(s,"*".join(s)))

def str_compare():
    """
    字符串比较原理：比较的是两个字符串的原始值ord(s),比较方式是逐个字符串进行比较
    ord(s)获取字符的原始值
    chr(s)获取原始值对应的字符串
    等值比较：比较的是内存地址
    :return:
    """
    print("'app'>'apple'比较的结果是%s："%("app">"apple"))
    print("'app'>'bug'比较的结果是%s："%("app">"bug"))
    print("字符串a的原始值是%s："%ord("a"))
    print("字符串b的原始值是%s："%ord("b"))
    print("原始值12345的对应的字符串是%s："%chr(12345))
    a = b = "python"
    c = "python"
    print("a和b是否相等%s"%(a == b))
    print("b和c是否相等%s"%(b==c))
    print("a的内存地址：%s\nb的内存地址：%s\nc的内存地址：%s\n"%(id(a),id(b),id(c)))
def str_format():
    """
    格式化字符串的第一种方式：%s、%f、%d
    格式化字符串的第二种方式：format
    格式化字符串的第三种方式：f"{n}"
    :return:
    """
    name = "张三"
    age = 18
    city = "北京"
    print("我的名字叫%s,今年%d岁,来自%s"%(name,age,city))
    print("我的名字叫{0},今年{1}岁,来自{2}".format(name,age,city))
    print(f"我的名字叫{name},今年{18}岁,来自{city}")

    print("我的名字叫%10s,今年%10d岁"%(name,age))  #10表示宽度
    print("圆周率的值是%10.2f"%3.1415926)   #.2表示保留2位小数，10表示后推10个占位符
    print("format表示圆周率是{0:10.2f}".format(3.1415926))     #.2f表示保留2位小数，10表示后推10个占位符

def str_encode():
    s = "天涯共此时"
    #编码
    print("%s  编码后的内容是：%s"%(s,s.encode("UTF-8")))
    byte = s.encode("UTF-8")
    #解码
    #byte表示二级制文件
    print("%s  解码后byte的内容是  %s"%(byte,byte.decode(encoding="UTF-8")))

if __name__ == '__main__':
    str_encode()