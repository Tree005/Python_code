#条件表达式(三元运算符)
#值1 if 条件 else 值2
#传统写法
age = 20
if age >= 18:
    text = '成年'
else:
    text = '未成年'

#条件表达式
text = '成年' if age >= 18 else '未成年'

#配合 lambda

is_adult = lambda age:'成年' if age >= 18 else '未成年'