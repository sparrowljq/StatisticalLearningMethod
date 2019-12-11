# Python中常用的数据类型
lst1 = list([1, 2, 3])
print(lst1)
# list末尾添加元素
lst1.append(4)
# 输出结果为 1 2 3 4
print(lst1)
# 在列表的末尾追加多个元素
lst1.extend([5, 6, 7])
# 1 2 3 4 5 6 7
print(lst1)

# 给给定位置的列表中添加元素
lst1.insert(1, 10)
# 输出结果为[1, 10, 2, 3, 4, 5, 6, 7]
print(lst1)
# 删除第一个出现的元素
lst1.remove(2)
# 输出结果为[1, 10, 3, 4, 5, 6, 7]
print(lst1)
# 删除列表中指定位置的元素，若未指定则默认删除最后一个元素
lst1.pop(1)
# 输出结果为[1, 3, 4, 5, 6, 7]
print(lst1)
# 返回1,5子序列中值为3的索引（子序列为可选参数）
tmp = lst1.index(3, 1, 5)
print(tmp)
# 递减排序
lst1.sort(reverse=True)
print(lst1)
# 反转列表中的元素
lst1.reverse()
# 输出结果为[1, 3, 4, 5, 6, 7]
print(lst1)
# 复制lst2
lst2 = lst1.copy()
# 输出结果为[1, 3, 4, 5, 6, 7]
print(lst2)
# 通过列表实现栈 “后进先出”
stack = [1, 2, 3]
stack.append(4)
# 输出结果为[1, 2, 3, 4]
print(stack)
stack.pop()
# 输出结果为[1, 2, 3]
print(stack)
# 尽管list可以实现队列的功能，但是在list从头插入一个元素时，效率较低需要移动其他元素因此可以通过collections.deque实现对列
# 对列的特点“先进先出”
from collections import deque
queue = deque([1, 2, 3])
queue.append(4)
queue.append(5)
queue.popleft()
queue.popleft()
print(queue)
# 列表的创建与使用
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

# 在py3中map()函数的返回值是一个对象，map(function,sequence) 函数的作用是把sequence中的值逐个传给function，返回一个包含函数执行结果的list
squares1 = list(map(lambda x: x**2, range(10)))
# 输出结果为 [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares1)
# 通过列表推导式来创建列表
squares2=[x**2 for x in range(10) if x>4]
# 输出结果为[25, 36, 49, 64, 81]
print(squares2)

# 两个for循环的列表推导式
squares3 = [(x**2, y**3) for x in [1, 2, 3] for y in [2, 3, 4] if x!= y]
# 输出结果为 [(1, 8), (1, 27), (1, 64), (4, 27), (4, 64), (9, 8), (9, 64)]
print(squares3)

# 以上的结果可以等价为
squares4 = []
for x in [1,2,3]:
    for y in [2,3,4]:
        if x!=y:
            squares4.append((x**2, y**3))
# 输出结果为[(1, 8), (1, 27), (1, 64), (4, 27), (4, 64), (9, 8), (9, 64)]
print(squares4)

# 列表操作的案例
exp1 = [-4, -2, 0, 2, 4]
tmp_exp_1 = [x*2 for x in exp1 if x>0]
# 输出结果为[4, 8]
print(tmp_exp_1)
tmp_exp_2 = [abs(x) for x in exp1]
# 输出结果为[4, 2, 0, 2, 4]
print(tmp_exp_2)
# 列表推导式可以包含复杂的表达式和嵌套函数
from math import pi
tmp_list = [str(round(pi, i)) for i in range(1, 6)]
# 输出结果为['3.1', '3.14', '3.142', '3.1416', '3.14159']
print(tmp_list)

# del声明
del_list = [0, 1, 2, 3, 4, 5, 6]
del del_list[3]
# 根据索引删除元素
print(del_list)
del del_list[3:6]
print(del_list)
# 删除这个列表元素
del del_list

# 元组和序列
# 一个元组包含多个用逗号分隔的值
# 元组与列表的对比 元组是不可变的，通常包含异类元素序列，这些元素可通过拆包或索引来访问
# 列表中的元素通常是同一类元素，列表是可变类型
t = 12345, 4566, 'hello'
print(t)
# 输出元组的第一个元素
print(t[0])
# 元组序列解压缩
# 序列解压缩要求等号左侧的变量数量与序列中元素的数量一样多
t = 12345, 4444, 'kobe'
z, x, y = t
print(z)

# python中的集合数据类型
# 说明创建一个集合数据类型必须使用set(), {}表示创建字典类型数据
box = {'apple', 'orange', 'apple', 'pear', 'banana'}
# 输出结果去掉重复的元素{'apple', 'orange', 'pear', 'banana'}
print(box)
print('apple' in box)

# 集合的交集、并集、差集、对称差
a = set('123456')
b = set('7345911')
# 输出结果为{'6', '5', '3', '4', '2', '1'}
print(a)
# 输出结果为{'9', '5', '3', '4', '7', '1'}
print(b)
# 输出结果为{'2', '6'}
print(a-b)
# a并b
# 输出结果为{'2', '3', '6', '9', '1', '4', '5', '7'}
print(a|b)
# a交b
# 输出结果为{'3', '5', '4', '1'}
print(a&b)
# 输出对称差
# 输出结果为{'2', '6', '9', '7'} 仅在a或仅在b中的元素
print(a^b)
# 集合元素支持列表推导式
exp_cel = {x for x in 'abcef' if x not in 'aef'}
# 输出结果为{'c', 'b'}
print(exp_cel)

# 字典数据类型
info = {'num': '1001', 'name': 'kobe', 'age': 32}
# 输出结果为kobe
print(info['name'])
# 删除num对应的键值对
del info['num']
info['name'] = 'james'
# 输出结果为{'name': 'james', 'age': 32}
print(info)
# 判断键是否在字典中
# 输出结果为True
print('name' in info)
# 返回键的list集合
key_list = list(info)
# 输出结果为['name', 'age']
print(key_list)
# dict() 函数直接从键-值对的序列构建字典
dict_list = dict([('jake', 1), ('marry', 2), ('sandy', 4)])
# 输出结果为{'jake': 1, 'marry': 2, 'sandy': 4}
print(dict_list)
# 字典支持列表推导式
dict_exp = {x: y for x in range(6) for y in range(3)}
# 输出结果为{0: 2, 1: 2, 2: 2, 3: 2, 4: 2, 5: 2}
print(dict_exp)
# 将关键字参数转换为字典
dict_exp1 = dict(name='aa',age='bb')
# 输出结果为 {'name': 'aa', 'age': 'bb'}
print(dict_exp1)
# 循环遍历字典类型数据
for k,v in dict_exp1.items():
    print(k,v)
# list遍历的技巧
# value-index 打印列表元素的值与索引
tmp_lst = list([1,2,3,4,5,6])
for i, v in enumerate(tmp_lst):
    print(i,v)
# 反向遍历list
for v in reversed(tmp_lst):
    print(v)
# 遍历排序集合
for v in sorted(tmp_lst):
    print(v)
# 可以同时遍历多个集合
lst_tmp1 = [1,2,3,4,5,6]
lst_tmp2 = ['a','b','c','d','e','f']
for a,b in zip(lst_tmp1,lst_tmp2):
    print(a,b)
# 输出结果为
# 1 a
# 2 b
# 3 c
# 4 d
# 5 e
# 6 f

