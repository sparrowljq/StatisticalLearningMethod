# Python函数
# Python提供了一种将定义放入文件中并在脚本或解释器的交互实例中使用他们的方法，这样的文件称为模块。
import MethodModel
# 调用模块方法
MethodModel.med1()
# 导入方法一
# from MethodModel import med1,med2
# 导入所有的模块
# from MethodModel import *
# 模块名称后跟as,则以下名称as将直接绑定到导入的模块
import MethodModel as method
method.med2()
# 将模块作为脚本执行

# 模块搜索路径
# 一些模块内置在解释器中，他们提供对操作的访问
import sys
# dir()函数列出了所有类型的名称：变量、模块、函数
lst = dir(MethodModel)
# 输出结果为['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'med1', 'med2']
print(lst)
# 输出结果为['D:\\Python\\StatisticalLearningMethod', 'D:\\Python\\StatisticalLearningMethod',
# 'E:\\Python\\python37.zip', 'E:\\Python\\DLLs', 'E:\\Python\\lib', 'E:\\Python',
# 'C:\\Users\\LJQ\\AppData\\Roaming\\Python\\Python37\\site-packages',
# 'E:\\Python\\lib\\site-packages']
# 该字符串确定解释器对模块的搜索路径，初始化为从环境变量获取默认路径PYthonPath
print(sys.path)
# 修改搜索路径
# sys.path.append('/usr/ss')

# dir()没有列出内置函数和变量的名称
import builtins
dir(builtins)

# 包
# 包是一种通过使用"点分模块名称"来构造Python模块名称空间的方法
