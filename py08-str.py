a = 'hello, '
print(type(a))  # <class 'str'>, 字符串是以字符为单位进行处理

a1 = a.encode()
print(type(a1))  # <class 'bytes'>, 以字节为单位进行处理

a2 = a1.decode()
print(type(a2))
print(a2)

s1 = 'this is a string'
s2 = s1.encode('utf-8')
print(type(s2))
print(s2)
s3 = s2.decode('utf-8')
print(type(s3))
print(s3)

# 1. + 可以用作字符串拼接
print(a + s1)  # hello, this is a string

# 2. * 重复输出
'''
python is a good language
python is a good language
'''

tmp = "python is a good language"
print((tmp + '\n') * 2)

# 3. 成员运算符
# 检查字符串中是否包含某个子字符串
# in: 如果包含的话，返回True,不包含返回False
# not in: 如果不包含的话，返回True，包含返回False

s = 'this is a string'
print('is' in s)  # True
print('str' in s)  # True
print('a' not in s)  # False
print('b' not in s)  # True

# 下标，python下标从0开始
# 作用是通过下标快速找到对应的数据
# 格式：字符串名[下标]

a = 'Chris'
print(a[0])  # C,从左往右取第一个字符
print(a[-1])  # s,从右往左取第一个字符
# print(a[5])  # IndexError: string index out of range， 超出下标范围报错

# 切片, 对操作的对象截取其中一部分的操作
# [开始位置:结束位置:步长], 包前不包后
# 步长:表示选取间隔,不写步长,则默认为1
# 步长的绝对值大小决定切取的间隔, 正负号决定切取方向
# 正数表示从左往右取值,负数表示从右往左取值

b = 'Hello Python'
print(b[0:4])  # Hell
print(b[1:3])  # el
print(b[4:])  # o Python, 截取下标为4之后的全部字符串
print(b[:4])  # Hell, 截取下标为4之前的全部字符串, 不包含下标4,包前不包后
print(b[-2:])  # on, 从倒数第2个下标开始,从左往右截取
print(b[-2:-5])  # 截取不到值, 因不截取方向不一致
print(b[-2:-5:-1])  # oht
print(b[-1::-1])  # nohtyP olleH, 从右往左截取
print(b[0::3])  # HlPh


# 1. 查询-find，查询字段符是否存在于目标字符串中，存在返回第一次出现位置的下标，不存在返回-1
# find(子字符串，[开始位置下标，结束位置下标])
# [开始位置下标，结束位置下标] 包前不包后
a = 'hello, python!'
print(a.find('t'))  # 9
print(a.find('t', 8))  # 9
print(a.find('t', 9))  # 9
print(a.find('t', 10))  # -1， 超出范围返回-1
print(a.find('py', 3, 8))  # -1， 超出范围返回-1
print(a.find('py', 3, 9))  # 7

# 1. 查询-index，查询字段符是否存在于目标字符串中，存在返回第一次出现位置的下标，不存在报错
# index(子字符串，[开始位置下标，结束位置下标])
# [开始位置下标，结束位置下标] 包前不包后

a = 'hello, Chris!'
print(a.index('el'))  # 1
# print(a.index('el', 8))  # ValueError: substring not found
# print(a.index('Ch', 3, 8))  # ValueError: substring not found
print(a.index('Ch', 3, 9))  # 7

# count(), 返回某个字符串在整个字符串中出现的次数，没有返回0
# count(子字符串，[开始位置下标，结束位置下标])
# [开始位置下标，结束位置下标] 包前不包后
c = '我命由我不由天'
print(c.count('我'))  # 2
print(c.count('我', 1))  # 1
print(c.count('我', 1, 3))  # 0

# startswith(), 判断是否以某个子字符串开头
# startswith(子字符串，[开始位置下标，结束位置下标])
# [开始位置下标，结束位置下标] 包前不包后
a = 'nothing is good, nothing is bad!'
print(a.startswith('no'))  # True
print(a.startswith('nh'))  # False
print(a.startswith('th', 2))  # True
print(a.startswith('th', 2, 3))  # False
print(a.startswith('th', 2, 4))  # True

# endswith(), 判断是否以某个子字符串开头
# endswith(子字符串，[开始位置下标，结束位置下标])
# [开始位置下标，结束位置下标] 包前不包后

print(a.endswith('d!', ))  # True
print(a.endswith('ing', 1, 6))  # False
print(a.endswith('ing', 1, 7))  # True