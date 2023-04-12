def printcoffee(*coffeename):  # 定义输出我喜欢的咖啡名称的函数
    print('\n我喜欢的咖啡有: ')
    for item in coffeename:
        print(item)  # 输出咖啡名称


printcoffee('蓝山')
printcoffee('蓝山', '卡布奇诺', '土耳其', '巴西', '哥伦比亚')
printcoffee('蓝山', '卡布奇诺', '曼特宁', '摩卡')
# 如果想要使用一个已经存在的列表作为函数的可变参数，可以在列表的名称前加"*"。来看下列代码：
# 定义一个列表
param = ['蓝山', '卡布奇诺', '土耳其']
# 通过列表指定函数的可变参数
printcoffee(*param)

