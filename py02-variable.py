# 定义变量的格式
# 变量名 = 值

num1 = 3
num2 = 10
total = num1 + num2
print("总价=", total)

num1 = "哈哈"  # 同一个变量可以被反复赋值，并且可以是不同的数据类型
print(num1)

# 标识符规定：
# 只能由数字，字母，下划线组成， python3支持用中文命名，但是不推荐，不符合代码规范性
# 不能以数字开头
# 不能是关键字
catch = "some thing"  # catch 在python中不是关键字
# 标识符包含在()中对标识符本身没有影响
(userName) = 'chris'
print((userName))

# 变量的命名规范，一种惯例，没有绝对民生或强制性的说法
# 1. 见名知意
name = 'chris'
# 2. 下划线分割法，python常用变量命名规则， 多个单词组成的变量，单词小写，单词间用下划线分割
user_name = 'John'
# 3. 大驼峰命名法
CountryName = 'China'
# 4. 小驼峰命名法
countryName = 'US'
