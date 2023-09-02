import matplotlib.pyplot as plt


def beautify_line_chart(x_start, x_end, y_start, y_end):
    # 添加标签
    plt.xlabel("x")
    plt.ylabel("f(x)")
    # 设置坐标轴范围
    px_start = x_start - 1
    py_start = y_start - 1
    px_end = x_end + 1
    py_end = y_end + 1
    plt.xlim(px_start, px_end)
    plt.ylim(py_start, py_end)
    # 设置横纵轴刻度
    plt.xticks([i for i in range(px_start, px_end)])
    plt.yticks([i for i in range(py_start, py_end)])
    # 添加网格线
    # plt.grid(True)
    # 横纵轴统一标尺
    plt.gca().set_aspect('equal', adjustable='box')
    # 显示图形
    plt.show()


def paint_dots_chart(x_lists, y_list):
    x_list = [x[1] for x in x_lists]
    plt.scatter(x_list, y_list)


def paint_line_chart(theta_matrix, x_start, x_end):
    x_array = np.linspace(x_start - 1, x_end + 1, 101)
    theta_list = theta_matrix.tolist()
    y_array = [x * theta_list[1][0] + theta_list[0][0] for x in x_array]
    plt.plot(x_array, y_array)
