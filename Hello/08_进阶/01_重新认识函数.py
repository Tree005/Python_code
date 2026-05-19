#函数也是对象
#def welcome():
#   print("你好呀，我是welcome函数")
#print(type(welcome))
#函数可外挂属性

#welcome.desc = '这是一个打招呼的函数'
#welcome.version = 1.0

#print(welcome.desc)
#print(welcome.version)

#函数赋值给变量
#say_hello = welcome#引用 不加括号 不加括号
#say_hello()

#函数可以作为参数传递给另一个函数
def caller(f):
    print('我要调用你了')
    f()
#caller(welcome)

#函数可以作为返回值
def welcome2():
    print("你好呀，我是welcome函数")
    def show_msg(msg):
        print(msg)
    return show_msg
result = welcome2()
result('你好我是返回函数')
result2 = welcome2#赋值
result2()('你好我是返回函数')