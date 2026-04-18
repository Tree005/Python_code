# None 是一个特殊的字面量，他表示空值 / 无值 / 无意义
msg = None

# None 的类型是 NoneType
print(type(msg))

# None 转为布尔值是 False
print(bool(msg))
if msg:
    print('你好')

# 不能参与数学运算，也不能与字符串拼接
 #result1 = msg + 1
 #result2 = msg + 'Hello'