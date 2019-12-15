# Python错误和异常
# 语法错误又称解析错误
# 异常 是指程序并无语法错误，但是程序执行时会引发错误，在执行时检测到的错误被称为异常
# ZeroDivisionError: division by zero
# a = 1/0
# 处理异常
try:
    a = 1/0
except ZeroDivisionError:
    print("分母不能为0")
# except子句可以将多个异常命名为带括号的元组
try:
    b = 1/0
    c = int('aa')
except(ZeroDivisionError, ValueError):
    print("程序处理异常")
# 如果发生的异常和except子句中的类是同一个类或者是它的基类，则异常和except子句的类是兼容的
class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass
# 打印的结果为B C D
for item in [B, C, D]:
    try:
        raise item()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
# 可以使用通配符捕获所有类型的异常
# 打印的结果是  程序执行异常
try:
    int('aa')
except ZeroDivisionError:
    print("分母不为0")
except:
    print("程序执行异常")

# 打印异常信息
import sys
try:
    int('aa')
except ZeroDivisionError as e:
    print("Exception info is {0}".format(e))
except:
    print(sys.exc_info()[1])
    print("程序执行异常")
# try……except 语句有一个可选的else子句，在使用必须放在所有的except子句后面。当try子句子句不引发异常时执行
# 执行结果是 程序执行正常
try:
   f = 'aa'
except ZeroDivisionError as e:
    print("Exception info is {0}".format(e))
except:
    print(sys.exc_info()[1])
    print("程序执行异常")
else:
    print("程序执行正常")
# 发生异常时，它可能具有关联值，也称为异常参数。参数的存在和类型取决于异常类型
# except子句可以在异常名称后面指定一个变量。这个变量和一个异常实例绑定，它的参数存储在instance.args中
# 异常实例定义了__str__(),因此可以直接打印参数而无需引用.args
# raise语句允许程序员强制抛出异常
try:
    raise Exception('aa', 'bb')
except Exception as e:
    print(type(e))
    # 输出异常参数('aa', 'bb')
    print(e)
    # 输出异常参数('aa', 'bb')
    print(e.args)
# 用户自定义异常 用户自定义异常必须继承异常类
class MyException(Exception):
    def __init__(self, expression, msg):
        self.expression = expression
        self.msg = msg
try:
    raise MyException('aa','bb')
except MyException as e:
    print(e.expression, " ", e.msg)
finally:
    print("不管怎样我都要执行")
# finally子句 无论程序是否发生异常都必须执行的语句，说明else子句是当try块中不发生异常才执行
# finally执行的复杂情况
# 如果在执行try语句时遇到一个break,continue或return语句，则finall子句将在执行break,continue或return语句之前被执行
# 如果finall子句中包含一个return语句，则finall子句的return语句将在执行try子句的return语句之前取代后者被执行
def test():
    try:
        return True
    finally:
        return False
# 打印结果是False
print(test())
# 如果在执行try子句期间发生了异常，该异常可由一个except子句处理，如果异常没有被except子句所处理，则该异常会在finall子句执行后被重新引发
# 如果异常发生在except子句中或else子句中，同样地该异常会在finall子句执行后重新引发


