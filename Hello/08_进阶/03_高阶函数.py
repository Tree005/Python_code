def info(msg):
    return '[提示]：' + msg
def warn(msg):
    return '[警告]：' + msg
def log(func,text):
    print(func(text)) # func 参数接收一个函数\
log(info,'文件保存成功')
log(warn,'磁盘空间不足')