import re


# 用于提取字符串中的数字
def handing(s):
    p_char_before = '[+-]?'  # 前置符号
    p_int = '\d+'  # 整数部分
    p_dot = f'[.]?'  # 小数点
    p_dot_int = '\d*'  # 小数部分
    pattern = f'{p_char_before}{p_int}{p_dot}{p_dot_int}'
    res = re.findall(pattern, s)
    return [float(num) for num in res]


if __name__ == '__main__':
    print(handing("h31100 23 cqt444.4 rabbit 11 2 dog 555.5"))
