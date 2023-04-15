import math  # 导入math模块


def circlearea(r):  # 计算圆的面积的函数
    result = math.pi * r * r  # 计算圆的面积
    return result  # 返回圆的面积


r = 10  # 半径
print('半径为', r, '的圆面积为: ', circlearea(r))
# lambda 使用匿名类的方式
result = lambda r: math.pi * r * r
print('半径为', r, '的圆面积为: ', result(r))
