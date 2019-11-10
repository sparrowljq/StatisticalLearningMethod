# 对偶感知机的代码
import numpy as np
import matplotlib.pyplot as plt

p_x = np.array([[3, 3], [4, 3], [1, 1]])
y = np.array([1, 1, -1])
# 绘制初始点
for i in range(len(p_x)):
    if y[i] == 1:
        plt.plot(p_x[i][0], p_x[i][1], 'ro')
    else:
        plt.plot(p_x[i][0], p_x[i][1], 'bo')
# 计算Gram矩阵
Gram = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
for i in range(len(p_x)):
    for j in range(len(p_x)):
        # dot函数表示矩阵的内积
        Gram[i][j] = np.dot(p_x[i], p_x[j])


# 初始化α1,α2,α3的值
afa = np.array([0, 0, 0])
# 初始化法平面截距
b = 0
# 初始化学习率η的值
delta = 1


while 1:
    # 用来表示所有的点是否被正分类
    choice = 1
    for i in range(len(p_x)):
        if y[i] == np.sign(np.dot(afa * y, Gram[i]) + b):
            continue
        while 1:
            # 只要进入该循环表示有点未正确分类
            choice = -1
            if y[i] == np.sign(np.dot(afa*y, Gram[i])+b):
                break
            else:
                afa[i] = afa[i]+delta
                b = b+delta*y[i]
    if choice == 1:
        break
print(afa)

w = np.dot(afa*y, p_x)
print(b)

line_x = [0, 10]
line_y = [0, 0]
for i in range(len(line_x)):
    line_y[i] = (-w[0]*line_x[i]-b)/w[1]

plt.plot(line_x, line_y)
plt.savefig("a.png")
plt.show()
