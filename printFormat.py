# 格式化输出
# 可以在{}应用变量的值
year = 2016
month = 10
str1 = f'Year is {year},month is {month}'
print(str1)

yes_votes = 42_575_654
no_votes = 43_132_495
print(yes_votes)
percentage = yes_votes / (yes_votes+no_votes)
print('{:9} Yes votes {:2.2%}'.format(yes_votes, percentage))
# format 函数的格式控制信息
# format()方法中的格式控制信息{<参数序号>:<格式控制标志>}
# ：<填充>         <对齐>     <宽度>      ，               <精度>          <类别>
#   用于填充      < 左对齐    输出宽度  数的千位         浮点数小数部分      整数类型
#   的单个字符    > 右对齐              分隔符          的精度或字符串      B，c,d,o,x,X
#                ^ 居中对齐          适用于整数、浮点数  的最大输出长度      浮点数类型 e,E,f,%
# b:输出整数的二进制 c:输出整数的对应Unicode d:输出整数十进制 o:输出八进制 x:小写十六进制 X：大写十六进制
# e:小写e字符对应的指数形式 E：大写字符对应的指数形式
f_str = 'kobe'
# 说明填充方式必须与对齐方式一起使用 如果不设宽度默认的填充宽度是0
# 输出结果为format out put-------------kobe-------------
print('format out put{:-^30}'.format(f_str))
# 表示的含义是用空格填充，左对齐
# 输出结果为kobe+'100个空格'
print('{0:100}'.format(f_str))
# '50个空格'+kobe+'50个空格'
print('{:^100}'.format(f_str))
data = 123456789.0555
# ----123,456,789----- ，表示千分位分隔
print('{0:-^20,}'.format(data))
# 输出结果为----123456789.06----
print('{0:-^20.2f}'.format(data))
# str()和函数repr()将任何值转化为字符串。str()函数是用于返回人类可读的值的表示，而repr()是用于生成解释器可读的表示。很多值使用任何一函数都
# 具有相同的表示，比如数字或类似列表和字典的结构。特殊的是字符串两个有不同的表示
aa = 123456
print('fff'+repr(aa))
# 输出结果为
# aaaa
# bbbbb
print(str('aaaa\nbbbbb'))
# 输出结果为'aaaa\nbbbbb'
print(repr('aaaa\nbbbbb'))
# repr()函数的参数可以是任意的Python类型
print(repr((3, 'a', ('dd', 'ee'))))
# 格式化字符串字面值
import math
print(f'The value of pi is approximately {math.pi:.3f}')
dict_data = {'jack': 4227, 'Jhon': 2334, 'kobe': 3344}
for k, v in dict_data.items():
    print(f'Name is {k:10}---->Value is {v:10d}')
# 其他修饰符可用于在格式化之前转化值。'!a'应用asscii(),'!s'应用str()，'!r'应用repr()
animals = 'eels'
# 输出结果为My favorate is eels
print(f'My favorate is {animals}')
# 输出结果为My favorate is eels
print(f'My favorate is {animals!s}')
# 输出结果为My favorate is 'eels'
print(f'My favorate is {animals!r}')
# 字符串的format()
# 输出结果为We are the aa who say bb
print('We are the {0} who say {1}'.format('aa', 'bb'))
# format()方法中使用关键字，引用的时使用关键字名称
print('We are the {name1} who say {name2}'.format(name1='aa', name2='bb'))
# 使用**符号传递关键字参数
table ={'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# 输出结果为Jack:4098; Sjoerd:4127; Dcab:8637678
print('Jack:{Jack:d}; Sjoerd:{Sjoerd:d}; Dcab:{Dcab:d}'.format(**table))

# format()函数的使用范例
for i in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(i, i**2, i**3))
# 手动格式化字符串
for k in range(1,11):
    print(repr(k).rjust(2), repr(k**2).rjust(3), repr(k**3).rjust(4))
# str.zfill() 他会在数字字符串的左边填充零，他能识别正负号
# 输出结果为00012
print('12'.zfill(5))
# 输出结果-03.14
print('-3.14'.zfill(6))

# open()返回一个文件对象
f = open('D:\\aa.txt', 'r+')
# 返回size个字符串
# print(f.read(10))
# 返回一行
#print(f.readline())
#循环遍历f
for line in f:
    print(line)
# 文件写入
f.write('This is test\n')
# 返回对象在文件中的当前位置
print(f.tell())



