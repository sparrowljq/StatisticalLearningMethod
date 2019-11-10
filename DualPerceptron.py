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
print(Gram)

# 初始化α1,α2,α3的值
afa = np.array([0, 0, 0])
# 初始化学习率η的值
delta = 1
# 超平面截距b
for i in range(100):
    # 用来表示所有的点是否被正分类
    choice = -1
    for j in  len(p_x):
        for k in range(100):
            if y[j]== np.sign(afa):


plt.show()
