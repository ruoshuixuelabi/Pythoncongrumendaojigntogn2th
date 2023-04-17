import re

pattern = r'[?|&]'
# 定义分隔符
url = 'http://www.mingrisoft.com/login.jsp?username="mr"&pwd="mrsoft"'
result = re.split(pattern, url)
# 分割字符串
print(result)
