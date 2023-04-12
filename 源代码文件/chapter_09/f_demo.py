message = '唯有在被追赶的时候，你才能真正地奔跑。'  # 全局变量
print('函数外部message =', message)


def f_demo():
    global message
    message = '命运给予我们的不是失望之酒，而是机会之杯。'  # 局部变量
    # 输出局部变量的值
    print('函数外部内部message =', message)


# 调用函数
f_demo()
# 在函数外部输出局部变量的值
print('函数外部message =', message)
