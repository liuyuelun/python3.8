
def set_create():
    #集合中元素不允许重复
    s = {1,2,3,3,4,5}
    print(s)
    #列表转换成集合，并去除重复元素
    l = [1,2,2,3,3]
    sl = set(l)
    print("列表l内容：",l)
    print("对列表l转换成集合后：",sl)
    #元组转成集合,集合内的元素是无序的
    st = set((12,2,2,4,5,65))
    print(st)
    #字符串转换成集合
    ss = set('python')
    print("python字符串，转换为集合后：",ss)
    #集合生成表达式：
    sss = {i*i for i in range(1,10)}
    print(sss)

def set_sql():
    s = {1,2,3,4,5}
    print(s)
    #集合添加一个元素
    s.add(6)
    print("使用add()添加一个元素6后：",s)
    #集合添加一个列表
    s.update([7,8,9])
    print("使用update()添加一个列表[7，8，9]后：",s)
    #一次删除一个指定元素，不存在抛异常.remove()
    try:
        s.remove(10)
    except Exception  as e:
        print(e)
    #一次删除一个指定元素，不存在不抛异常.discard()：
    s.discard(10)
    #随机删除一个集合元素
    s.pop()

def set_compare():
    #两个集合元素相同，则集合相同
    s1 = {10,20,30,40}
    s2 = {30,10,20,40}
    s3 = {10,30,50}
    s4 = {20,50}
    print("%s和%s是不是相等："%(s1,s2),s1 == s2)
    #一个集合是不是另一个集合的子集，
    print("%s是不是%s的子集："%(s3,s1),s3.issubset(s1))
    #一个集合是不是另一个集合的超集
    print("%s是不是%s得超集："%(s1,s3),s1.issuperset(s3))
    #两个集合是不是有交集
    print("%s和%s是不是有交集："%(s3,s4),s3.isdisjoint(s4))
    #求两个集合的交集:intersection
    print("%s和%s的交集是："%(s1,s4),s1.intersection(s4))
    print("%s和%s的交集是："%(s1,s4),s1&s4)
    #求两个集合的并集：
    print("%s和%s的并集是："%(s3,s4),s3.union(s4))
    #求两个集合的差集操作：
    print("%s和%s的差集是："%(s2,s3),s2.difference(s3))
    print("%s和%s的差集是："%(s2,s3),s2-s3)
    #求两个集合的对称差集：
    print("%s和%s的对称差集是："%(s2,s3),s2.symmetric_difference(s3))





if __name__ == '__main__':
    set_create()