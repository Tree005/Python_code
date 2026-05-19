# 多返回值 返回元组类型
def  calculate(x,y):
    res1 = x + y
    res2 = x - y
    return res1,res2
result = calculate(30,10)
print(result)
print(type(result))
#元组拆包
r1,r2 = calculate(30,10)
print(r1)
print(r2)
#*args 把所有传进来的位置参数打包成一个元组
# **kwargs — 打包关键字参数
def show_info(*args,**kwargs):
    print('位置参数：',args)
    print('关键字参数：',kwargs)
show_info(10,20,30,name = '张三',age = 18)

#解包传递参数
nums = (10, 20, 30)
person = {'name': '张三', 'age': 18, 'gender': '男'}
show_info(*nums,**person)
