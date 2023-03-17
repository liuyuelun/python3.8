
class Student():
    """
    类由一个或多个单词组成，每个单词的首字母需要大写
    """
    l = []    #直接定义在类里面的属性，称为类属性
    def __init__(self,name):
        self.name = name,

    #实例方法
    def name_method(self):
        print("我的名字是：{0}".format(self.name))

    #静态方法
    @staticmethod
    def method():
        print("我使用了staticmethod进行了修饰，所以我是个静态方法")

    #类方法
    @classmethod
    def cls_method(cls):
        print("我使用了classmethod进行了修饰，所以是个类方法")

if __name__ == '__main__':
    print(Student("张三").name_method())  