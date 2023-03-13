def list_l():
    #创建列表的第一种方式[]
    l = ["hello","world",99]
    print(id(l))
    print(type(l))
    print(l)
    #创建列表的第二种方式list()
    lst = list(['hello','kitty'])
    print(lst)
    #列表表达式：
    ll = [i*i for i in range(1,11)]
    print(ll)

def element_find_ndex():
    list = ['hello','world',99,"hello"]
    #list.index(element):如果列表中存在多个相同元素，只返回列表第一个元素的索引值
    print(list.index("hello"))
    #如果列表不存在索引元素，："value error"错误
    try:
        list.index(100)
    except ValueError as e:
        print(e)
    #在指定区间查找指定元素的索引
    print(list.index("hello",1,4))

def index_find_element():
    #获取指定索引的元素值
    list = ["hello","world",100,"hello"]
    print(list[3])
    #获取的索引值超出列表长度时，报"IndexError"错误
    try:
        print(list[5])
    except IndexError as i:
        print(i)
    #获取元素中的多个元素：[start:stop:step]
    l = [1,2,3,4,5,6,7,8,9,10]
    print(l[1:9:2])

def for_list():
    list = [1,2,3,4,5,6,7,8,9,10]
    for i in list:
        if i in list:
            print(list.index(i))

def list_sql():
    l = [10,20,30,40,50]
    l1 = [1,2,3]
    print("添加元素之前：",l,id(l))
    #列表追加元素
    l.append(60)
    print("添加元素之后：",l,id(l))
    #列表尾部追加多个元素
    l.append(l1)
    print("添加多个元素后：",l,id(l))
    #列表指定位置插入一个元素,原有位置元素进行后推：
    l.insert(0,11)
    print("在0号索引位插入一个元素后：",l,id(l))
    #列表任意位置替换多个元素：
    l[1:] = l1
    print("在1号索引位后，替换原有元素：", l, id(l))
    #删除列表指定元素，如果存在多个，只删除第一个元素
    l.remove(2)
    print("删除元素2后：", l, id(l))
    #删除列表指定索引值的元素
    l.pop(2)
    print("删除2号索引位的元素之后，：", l, id(l))

def list_sort():
    #sort():对原列表所有元素进行从小到大进行排序，可以指定reverse=True,进行倒序排序
    l = [9,3,6,8,4,1,4,6,7,97,5,4,3]
    l.sort(reverse=True)
    print("倒序排列：",l)
    l.sort()
    print("正序排列：",l)
    #sorted():对列表进行排序，指定reverse=True，可以进行降序排列，原列表不发生改变
    l0 = [9,3,45,7,1,5,6,7,1,9]
    l1 = sorted(l0,reverse=True)
    print("倒序排列后的列表：",l1)
    l2 = sorted(l0,reverse=False)
    print("正序排列后的列表：",l2)
    print("sorted后的原列表l",l0)

if __name__ == '__main__':
    list_sort()