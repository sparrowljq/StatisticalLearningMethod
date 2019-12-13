# 格式化输出
# 可以在{}应用变量的值
year = 2016
month = 10
str = f'Year is {year},month is {month}'
print(str)

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
