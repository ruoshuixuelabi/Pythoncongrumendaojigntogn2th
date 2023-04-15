import re

pattern = r'mr_\w+'  # 模式字符串
string = 'MR_SHOP mr_shop'  # 要匹配的字符串
match = re.search(pattern, string, re.I)  # 搜索字符串，不区分字母大小写
print(match)  # 输出匹配结果
string = '项目名称MR_SHOP mr_shop'
match = re.search(pattern, string, re.I)  # 搜索字符串,不区分字母大小写
print(match)  # 输出匹配结果
