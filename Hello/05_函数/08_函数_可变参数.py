# 可变位置参数：定义函数时在形参名前加'*'可以接收 任意数量 的位置参数，并打包成一个元组(ages的数据类型为：元组)

def test1(*ages):
    print(f'年龄为：{ages}')
test1('你好','男',18,178)

# 可变关键字参数：定义函数时在形参名前加'**'可以接收 任意数量 的关键字参数，并打包成一个字典(kwargs的数据类型为：字典)

def test2(**kwargs):
    print(f'年龄为：{kwargs}')
test2(name='你好',gender='男',age=18,height=178)

# 可变位置参数，可变关键字参数，可以同时使用，但必须先写可变位置参数
def test3(*args,**kwargs):
    print(args)
    print(kwargs)
test3(18,'男',name='Tree',height=178)

# 可变位置参数，可变关键字参数，也能与其他类型参数同时使用
def test4(a,b,*args,c='关键字参数',**kwargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(kwargs)
test4('张三','抽烟','喝酒','打牌',c='赌博',age=18,name='李四')
