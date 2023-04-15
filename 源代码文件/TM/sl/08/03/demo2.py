import re

pattern = r'[1-9]{1,3}(\.[0-9]{1,3}){3}'  # 模式字符串
str1 = '127.0.0.1 192.168.1.66'  # 要配置的字符串
match = re.findall(pattern, str1)  # 进行模式匹配
print(match)
