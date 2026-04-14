def greet(name,gender,age,height):
    print(f'我是{name},性别{gender}今年{age}岁,身高{height}cm')

#正确调用
#greet('Tree','man',20,178)

#错误调用
greet('Tree',20,178)
greet('nan','Tree',178,20)