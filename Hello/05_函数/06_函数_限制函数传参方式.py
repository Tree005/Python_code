#使用 / 和 * 限制传参方式
# / 必须放在 * 之前
def greet(name,/,gender,*,age,height):
    print(f'你好我是{name},性别{gender},今年{age},身高{height}')

# / 前只能用位置参数 * 后只能用关键字参数 
#/ * 中间的参数使用位置参数,关键字参数均可
greet('Tree','男',age=18,height=178)
greet('Tree',gender='男',age=18,height=178)

#错误调用
#greet(name='Tree','男',age=18,height=178)
#greet(name='Tree',gender='男',age=18,height=178)
#greet('Tree',gender='男',18,height=178)