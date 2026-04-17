#定义函数（设置参数默认值）
# 可选参数必须放在最后
def greet(name,gender,age,height,msg='你好'):
    print(f'我是{name},性别{gender},今年{age},身高{height}')
    print(f'我想所：{msg}')

#调用参数
#greet('Tree','男',20,178)
#greet('Tree','男',20,178,'Hello')
#greet('Tree','男',20,178,msg='Hello')

# print()函数底层给 and参数 设置了默认值
print('你好')
print('我不好',end='!!')
