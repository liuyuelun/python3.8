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


if __name__ == '__main__':
    str_is()