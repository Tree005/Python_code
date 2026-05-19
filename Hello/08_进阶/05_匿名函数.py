'''
#lambda 匿名函数
语法： lambda 参数: 表达式
  - 冒号左边是参数，右边是返回值表达式
  - 表达式结果自动 return，不用写 return
  - 只能写一行，不能写 if/for/while 代码块'''
'''
普通写法
def add(x,y):
    return x + y
'''
#lambda 写法
add = lambda x,y : x + y
print(add(10,20))
# 配合高阶函数使用
def calculate(func,a,b):
    print(f'计算结果：{func(a,b)}')
calculate(lambda x,y:x + y,30,10)
calculate(lambda x,y:x - y,30,10)
