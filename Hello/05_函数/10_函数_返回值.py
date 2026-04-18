# 无返回值
def add1(n1,n2):
    print(f'我收到了：{n1},{n2},二者相加为：{n1 + n2}')

# 调用函数
result1 = add1(100,200)
print(result1)
# print()函数是没有返回值的
#res = print('Hello')
print('----------------------------')
# 有返回值
def add2(n1,n2):
    print(f'我收到了：{n1},{n2},二者相加为：{n1 + n2}')
    answer = n1 + n2
    return answer
    print('Return 后的语句不执行')

result2 = add2(100,100)
print(result2)