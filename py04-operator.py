# 1. 数算运算符 【+-*/%】
print(1 / 1)  # 输出：1.0, 除法结果 为浮点数
a = 1 / 2
print(type(a))  # 输出：<class 'float'>

# 取整除，结果取整数部分，向下取整，只要有小时就忽略小数
a = 5
b = 2
print(a // b)  # 输出：2

# 取幂，m的n次方
m = 2
n = 4
print(m ** n)  # 输出：16

# 使用算术运算术时，其中若有浮点数，结果一定用有浮点数表示
print(7.1 // 2)  # 输出：3.0

# 运行规则 ： 幂是最新优先级，然后先乘除后加减，同级运算从左往右，可以用()调整计算的优先级
print(2 ** 3 + 4 * 5)  # 28

# 2. 赋值运算符 【=，-=，+=】
# 3. input() 输入函数
# v = input("pls input:")
# print(v)

# 4.转义字符
# \t 制表符表示空四个空格也称缩进
print("chris\t12345")  # chris	12345

# \n 换行
# \r 回表，表示将当前位置移动本行开头
print("aaa\rbbb")  # 输出：bbb

# \\ 反斜杠符号
print("hello\\there")  # hello\there
print(r'I am chris\\\1212')  # 输出：I am chris\\\1212， r表示输出原生字符串，不转义

# 5. 比较运算符【==,!=,>,<,>=,<=】
c = 1212
d = 2343
e = 12
f = 32
print(a > d)  # False

if c < d:
    print(True)
else:
    print(False)

# 6. 逻辑运算符【and,or,not】
if c > d or e < f:
    print(True)

if not c > d:
    print("c小于d")

# 7. 三目运算符【为True时的结果 if a<b else 为False时的结果】
a = 2
b = 12
result = 'a<b' if a < b else 'a>=b'
print(result)  # 输出：a<b
