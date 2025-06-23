def add(a, b):
    return a + b


# 定义一个函数，用于计算两个数的乘积
def mul(a, b):
    return a * b


if __name__ == "__main__":  # 加上该语句别人在导入时就不会执行该模块内的运算
    # 调用add函数计算20+30的结果并打印输出
    # 这里演示了模块内部测试add函数的功能
    print(add(20, 30))
    print(mul(20, 30))  # 调用mul函数计算20*30的结果并打印输出
