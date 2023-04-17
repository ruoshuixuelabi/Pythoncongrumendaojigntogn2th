import re

pattern = r'1[34578]\d{9}'
# 定义要替换的模式字符串
string = '中奖号码为:84978981联系电话为:13611111111'
result = re.sub(pattern, '1XXXXXXXXXX', string)
# 替换字符串
print(result)
