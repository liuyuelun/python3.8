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
