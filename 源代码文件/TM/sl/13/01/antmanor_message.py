print("\n", "=" * 10, "蚂蚁庄园动态", "=" * 10)
file = open('message.txt', 'w')  # 创建或打开保存蚂蚁庄园动态信息的文件
print("\n 即将显示……\n")
file = open('picture.png','rb')	#以二进制方式打开图片文件
print(file) # 输出创建的对象
# 以下为关闭文件对象的代码
# file.close()    # 关闭文件对象
