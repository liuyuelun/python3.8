users = {}  # 用字典存储用户信息，键为用户名，值为密码


def register(username, password):
    """注册函数"""
    if username in users:
        print("用户名已存在")
    else:
        users[username] = password
        print("注册成功")


def login(username, password):
    """登录函数"""
    if username not in users:
        print("用户名不存在")
    elif users[username] != password:
        print("密码错误")
    else:
        print("登录成功")


# 测试代码
register("user1", "123456")
login("user1", "123456")
login("user1", "654321")
register("user1", "111111")
