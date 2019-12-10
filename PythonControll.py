# python 流程控制

# if
x = 3
if x < 0:
    print("小于0")
elif x==0:
    print("等于0")
else:
    print("大于0")
# for循环
words = ['cat', 'dog', 'pig']
# 遍历方法一
for item in words:
    print(item)
# 遍历方法二
for item in range(len(words)):
    print(item, words[item])
# for循环遍历数列
# 输出结果为5 6 7 8 9不包括10
for i in range(5, 10):
    print(i)
# 5 7 9
for i in range(5, 10, 2):
    print(i)

# 循环语句中可以带一个else语句，当循环体执行完毕跳出循环时执行（通过break方法跳出循环时不执行）
# break表示结束循环，continue表示跳出本次循环
for n in range(2, 10):
    for x in range(2, n):
        if n%x == 0:
            # // 取整数除法（向下取整）
            print(n, '=', x, '*', n//x)
            break
    # 此else属于for循环
    else:
        print(n, "是素数")
# pass声明 pass不执行任何操作，仅是占位符的作
# 说明： 在定义循环、方法、类时若出现空方法体、空循环时必须用pass
# while True:
#    pass

# 定义函数
def fib():
    print("This is my first method")
# 调用函数
fib()
# 定义带有返回值的函数
def med1(n):
    return n+1
print(med1(5))

# 定义默认值参数的函数
def med2(a, b=3):
    print(a+b)
# 调用方法一
med2(2)
# 调用方法二
med2(3, 5)

# 默认值仅被评估一次，当默认值为可变对象时（如，列表字典）会有所不同
def med3(a,L = []):
    L.append(a)
    return L
# 输出结果为1
print(med3(1))
# 输出结果为1 2
print(med3(2))
# 输出结果为 1 2 3
print(med3(3))

# 如果不希望共享默认值
def med4(a,L=None):
    if L is None:
        L=[]
    L.append(a)
    return L
# 输出结果为1
print(med4(1))
# 输出结果为2
print(med4(2))
# 输出结果为 3
print(med4(3))

# 关键字参数
def med5(num,name="kobe",age=12):
    print(num, " ", name, " ", age)

med5(100)
med5(100, 'james', '35')

# 解压缩参数列表
l1 = list(range(3, 6))
# 输出结果为3 4 5
print(l1)
# 当参数在列表或元组中时，可以用*-operator编写函数调用
args = [3, 6]
l2 = list(range(*args))
print(l2)
# 当参数列表在字典中时通过**-operator传递关键字参数
arg = {"num": "100", "name": "james", "age": "34"}
med5(**arg)

# lambda表达式
p = lambda x, y: x+y
# 输出结果为5
print(p(2, 3))

# lambda表达式的另一个作用是传递一个小的函数作为参数
tmp = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
tmp.sort(key=lambda tmp:tmp[1])
print(tmp)