# python数字运算
# 输出2+2的结果
print(2+2)
# 输出17%3的结果
print(17% 3)
# 输出5**2的幂运算
print(5**2)
# 定义数字类型的变量
width = 10
heith = 20
s = width * heith
print(s)
# 四舍五入浮点数
res = round(133.0655, 2)
print(res)
# python对字符串的支持
# python中的字符串是不变的，不能更改字符串中的内容
# python操作字符串可以用单引号或双引号括起来 \号可以用来转义引号
s = "This is my first Python program"
print(s)
# 输出结果This is a 'dog'
s = "This is a \'dog\'"
print(s)
# 如果不希望\为特殊字符可以在字符串之前添加一个原始字符串来使用原始字符串
# 输出的结果为This is a \'dog\'
s = r"This is a \'dog\'"
print(s)

# 多行字符串的使用''' '''及""" """
print('''
usage: thingy [options]
-h
-H hostname
''')
# 字符串拼接以及多次输出字符串
# 输出结果kobekobekobejames
s = 3*'kobe'+"james"
print(s)

# 相邻的两个或多个字符串文字会自动连接在一起
# 输出结果为python
s = 'py' 'thon'
print(s)

# 断开长字符串
# 输出结果为Put several strings within parenthesesto have them joined together.
text = ('Put several strings within parentheses'
        'to have them joined together.')
print(text)

# 字符串拼接
prefix = 'Py'
print(prefix+'thon')
# 输出字符串的某个字符
word = 'Python'
# 输出结果P
print(word[0])
# 从右边开始计算输出结果为o
print(word[-2])
# 对字符串切片
# 范围是左闭右开 输出结果为Py
print(word[0:2])
# 从下标为2的字符开始，直到字符串结束
print(word[2:])
# 从字符串开始到下标为2,左闭右开 输出结果为Py
print(word[:2])
# 从右边开始计算到字符串结束 输出结果为on
print(word[-2:])

# 返回字符长度
print(len(word))
# 字符串常用的方法略

# Python支持list
arrayList = [1, 2, 3, 5, 4]
print(arrayList)
# 从下标为3开始获取list集合中的值
print(arrayList[3:])
# 列表与字符串不同，可以改变列表中的内容
arrayList[0] = 10
print(arrayList)
# 向列表中末尾添加元素
arrayList.append(22)
print(arrayList)
# 通过切片更改列表中的元素
arrayList[2:4] = [100, 1000]
print(arrayList)

# 通过切片来清除列表中的元素
arrayList[2:4] = []
print(arrayList)
# 计算列表中元素的个数
print(len(arrayList))

# 嵌套列表
a = [1, 2, 3, 4]
b = ['a', 'b', 'c']
x = [a, b]
# 输出的结果为[[1, 2, 3, 4], ['a', 'b', 'c']]
print(x)
# 输出的结果为b
print(x[1][1])

# Fibonacci series
a, b = 0, 1
while a < 10:
    # 输出的结果为0,1,1,2,3,5,8,
    print(a, end=',')
    a, b = b, a+b
# 输出结果为The value of i is 256
print("The value of i is", 256)
