import re


# 用于提取字符串中的数字
def extract_number_from_str(s):
    p_char_before = '[+-]?'  # 前置符号
    p_int = '\d+'  # 整数部分
    p_dot = f'[.]?'  # 小数点
    p_dot_int = '\d*'  # 小数部分
    pattern = f'{p_char_before}{p_int}{p_dot}{p_dot_int}'
    res = re.findall(pattern, s)
    return [float(num) for num in res]


# 读取纯数据集
def read_data_set_file(file_path):
    data_list = []
    with open(file_path, 'r') as f:
        for line in f.readlines():
            line = line.rstrip()
            line_data = extract_number_from_str(line)
            data_list.append(line_data)
    return data_list


# 读取样本数据集，单行格式为：x1 x2 ... y
# 返回x和y矩阵
def read_xy_data_set_file(file_path):
    data_list = []
    y_list = []
    i = 0
    with open(file_path, 'r') as f:
        for line in f.readlines():
            line = line.rstrip()
            line_data = extract_number_from_str(line)
            data_list.append([1])
            y_list.append([])
            data_list[i].extend(line_data[:-1])
            y_list[i].append(line_data[-1])
            i = i + 1
    return data_list, y_list


# 读取混合数据集，抽取其中的数字
def read_data_set_file_not_pure(file_path):
    data_list = []
    with open(file_path, 'r') as f:
        for line in f.readlines():
            line = line.rstrip()
            line_data = extract_number_from_str(line)
            if len(line_data) == 0:  # 该行无数字，可能为注释或文字说明
                continue
            data_list.append(line_data)
    return data_list


# 读取数据集字符串
# 返回x和y矩阵
def read_xy_data_set_str(s):
    data_list = []
    y_list = []
    i = 0
    for line in s.splitlines():
        line = line.rstrip()
        line_data = extract_number_from_str(line)
        data_list.append([1])
        y_list.append([])
        data_list[i].extend(line_data[:-1])
        y_list[i].append(line_data[-1])
        i = i + 1
    return data_list, y_list


# 读取混合数据字符串，抽取其中的数字
def read_data_set_str_not_pure(s):
    data_list = []
    for line in s.splitlines():
        line_data = extract_number_from_str(line)
        if len(line_data) == 0:  # 该行无数字，可能为注释或文字说明
            continue
        data_list.append(line_data)
    return data_list
