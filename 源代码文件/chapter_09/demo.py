# 定义函数
def demo(obj):
    print("原值:", obj)
    obj += obj
# 调用函数
print("=========值传递========")
mot = "唯有在被追赶的时候,你才能真正地奔跑。"
print("函数调用前: ", mot)
demo(mot)  # 采用不可变对象——字符串print("函数调用后: ",mot)
print("=========引用传递========")
list1 = ['绮梦', '冷伊一', '香凝', '黛兰']
print("函数调用前:", list1)
demo(list1)  # 采用可变对象——列表
print("函数调用后:", list1)
