def greet(name,gender,age,height):
    print(f'我是{name},性别{gender},今年{age},身高{height}')
#使用关键字参数

greet(name='Tree',gender='男',age=18,height=178)
greet(height=178,name='Tree',gender='男',age=18)
greet('Tree','男',height=178,age=18)

#错误调用:位置参数必须放在关键字参数之前
#greet(name='Tree','男',18,178)
#greet(name='Tree','男',age=18,178)
#greet(name='Tree',age=18,'男',178)
#greet('男',178,name='Tree',age=18)

#意外参数
#greet(name='Tree',gender='男',age=18,height=178,shcool='森林幼儿园')
#重复参数
#greet(name='Tree',gender='男',age=18,height=178,age=18)

