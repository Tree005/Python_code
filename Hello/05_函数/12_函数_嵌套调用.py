# 嵌套调用：在一个函数执行的过程中，调用另一个函数

def test1():
    print('进入test1函数')
    test2()
    print('退出test1函数')

def test2():
    print('进入test2函数')
    test3()
    print('退出test2函数')

def test3():
    print('进入test3函数')
    print('test3函数正在执行')
    print('退出test3函数')
test1()