def filterchar(string):
    """功能:过滤危险字符（如黑客)，并将过滤后的结果输出
        about:要过滤的字符串
        没有返回值
    """
    import re  # 导入Python的re模块
    pattern = r'(黑客)|(抓包)|(监听)|(Trojan)'  # 模式字符串
    sub = re.sub(pattern, '@_@', string)
    # 进行模式替换
    print(sub)


if __name__ == '__main__':
    about = '我是一名程序员，喜欢看黑客方面的图书，想研究一下Trojan。'
    filterchar(about)
