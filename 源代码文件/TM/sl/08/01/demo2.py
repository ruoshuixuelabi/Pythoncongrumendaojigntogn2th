import re

pattern = r'mr_\w+'
# 模式字符串
string = 'MR_SHOP mr_shop'
# 要匹配的字符串
match = re.match(pattern, string, re.I)
# 匹配字符串，不区分字母大小写
print('匹配值的起始位置: ', match.start())
print('匹配值的结束位置: ', match.end())
print('匹配位置的元组: ', match.span())
print('要匹配的字符串: ', match.string)
print('匹配数据: ', match.group())
