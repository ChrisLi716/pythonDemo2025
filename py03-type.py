# 数值类型
# int(整型)
num = -3
# <class 'int'>
print(type(num))  # 判断数据类型的方法 type()

# float(浮点型)
a = 1.5
# <class 'float'>
print(type(a))

# bool(布尔性)， 真为True，假为False， True相当于整数1，False相当于整数0
print(True + False)  # 1
# True和False必须严格区分大小写，不然报错
# print(false)  # NameError: name 'false' is not defined

# complex复数型
# 固定写法 ， z = a + bj, a是实部， b是虚部， j是固定虚部单位不能变
print(type(2 + 3j))  # <class 'complex'>

ma = 1 + 2j
mb = 2 + 3j
print(ma + mb)  # (3+5j)

# 字符串类型，单引号和双引号都可以，包含多行时使用三个双引号
s = """
你好
这是一个多行字符串
"""
print(s)

# 格式化输出
# 1. %s(字符串)
name = 'chris'
age = 36
print("userName:%s" % name)  # userName:chris
print("userName:%s, age:%d" % (name, age))  # userName:chris, age:36

b1 = 789
print("value:%-10s" % b1)  # value:789       ， 左对齐，占位符10位
print("value:%10s" % b1)   # value:       789， 右对齐，占位符10位

# 2. %d(整数)
a = 123
print("%d" % a)  # 原样输出123
print("%6d" % a)  # 输出6位数字，不够时前端补空格，当超出时原样输出，   123
print("%06d" % a)  # 输出6位数字，不够时前端补0，当超出时原样输出，000123

# 3. %d(浮点型)
a = 1.2345678
print("%f" % a)  # 1.234568， 默认后面六位小数，遵循四舍五入
b = 2.3456789
print("%3f" % b)  # 2.345679， 默认后面六位小数，遵循四舍五入
print("%.3f" % b)  # 2.346， .3f表示后面保留3位小数，遵循四舍五入
print("%.10f" % b)  # 2.3456789000， .3f表示后面保留10位小数，不够时前端补0，遵循四舍五入

# 4. %%
print('name %% , age 1%%' % ())  # name % , age 1%, %%输出一个%字符

# 5. f-strings (格式化字符串字面量)
name = 'chris'
age = '32'
print(f'name:{name},age:{age}')  # name:chris,age:32

# 6. {} (花括号占位符)Python 3.6版本开始引入的一种新语法
# 基本用法
name = "John"
age = 25

print("My name is {} and I am {} years old.".format(name, age))

# 位置
h = 'every one'
formatted_string = "hello: {2}, Name: {0}, Age: {1}".format(name, age, h)
print(formatted_string)  # 输出:hello: every one, Name: John, Age: 25

# 关键字参数
formatted_string = "Name: {name}, Age: {age}".format(name="Carol", age=28)
print(formatted_string)  # 输出: Name: Carol, Age: 28
