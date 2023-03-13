def dict_create():
    #大括号创建字典
    a = {"a":"1","b":"2"}
    #dict()函数创建字典
    b = dict(c=3,d=5)
    print(a,"\t",type(a))
    print(b, "\t", type(b))
    #字典生成表达式：
    c = ["Tom","Jack","Lily"]
    d = [21,25,28]
    dt = {k:v for k,v in zip(c,d)}
    print("列表c：",c)
    print("列表d：",d)
    print("列表c和列表d生成的字典：",dt)

def dict_get():
    a = {"张三":"100","李四":"200","王五":"300","赵六":"400"}

    #获取字典的值
    print("张三：",a["张三"])
    print("李四：",a.get("李四"))
    #使用dict.get(key,value)进行查找时，key不存在时，会返回value
    print("麻七",a.get("麻七：","不存在麻七"))
    #获取字典中所有的key：
    print("字典中所有的key：",list(a.keys()))
    #获取字典中所有的values：
    print("获取字典中所有的values：",list(a.values()))
    #获取字典中所有的键值对：
    print("字典中所有的键值对：",list(a.items()))

def dict_add_del():
    a = {"张三": "100", "李四": "200", "王五": "300", "赵六": "400"}
    #删除指定键值对：del a["张三"]
    #清空字典：a.clear()
    a["马七"] = 500  #新增元素
    print(a)
    a["赵六"] = 399   #修改元素
    print(a)

def dict_for():
    a = {"张三": "100", "李四": "200", "王五": "300", "赵六": "400"}
    for i in a:
        print(i+":"+a[i])


if __name__ == '__main__':
    dict_create()