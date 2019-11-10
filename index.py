#原始感知机代码
import numpy as np
import matplotlib.pyplot as plt
# 输入三个点x1(3,3)、x2(4,3)、x3(1,1)其中x1,x2为正实例点，x3为负实例点
p_x = np.array([[3, 3], [4, 3], [1, 1]])
y = np.array([1, 1, -1])
# 绘制初始点
for i in range(len(p_x)):
    if y[i] == 1:
        # r表示红色 o表示圆点
        plt.plot(p_x[i][0], p_x[i][1], 'ro')
    else:
        # b表示蓝色 o表示圆点
        plt.plot(p_x[i][0], p_x[i][1], 'bo')
# w超平面的法向量,b是超平面的截距，delta是指的是学习率
w = np.array([0, 0])
b = 0
delta = 1

for i in range(100):
    choice = -1
    for j in range(len(p_x)):
        # dot函数表示向量点积
        if y[j] != np.sign(np.dot(w, p_x[j]) + b):
            choice = j
            break
    # 表示三个点都被正确分类
    if choice == -1:
        break
    w = w + delta * y[choice] * p_x[choice]
    b = b + delta * y[choice]

line_x = [0, 10]
line_y = [0, 0]
print(w[1])
# 超平面表达式为wx+b=0 其中w为向量 w1x1+w2x2+b=0 x2=(-w1x1-b)/w2
for i in range(len(line_x)):
    line_y[i] = (-w[0] * line_x[i] - b) / w[1]
    print(line_y)


plt.plot(line_x, line_y)
plt.savefig("picture.png")
plt.show()