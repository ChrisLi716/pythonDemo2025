# 元组
# 格式：元组名=(元素1,元素2,元素3...)
# 所有的元素都在小括号里，元素间用逗号分开，元素类型可以相同也可以不同
# 元组只支持查询不支持修改

tup = (1, 2, 3, 4, 'a', True)
tup2 = (1,)  # 如果元素只有一个元素，后面加上逗号，不然当作整形处理
print(type(tup))  # <class 'tuple'>
print(type(tup2))

# 元组也有下标，从0开始
a = tup[1]
print(a)

# 元组只支持查询不支持修改
# tup[1] = 'a'  # TypeError: 'tuple' object does not support item assignment

# count(), index(), len()和列表的用法相同

tup = (1, 2, 3, 4, 'a', '2', 3, True)
print(tup[0])  # 1
print(tup[2])  # 3
print(tup.count(3))  # 2
print(len(tup))  # 8

# 元组的应用场景
# 1. 函数的参数和返回值
# 2. 格式化输出
name = 'chris'
age = 23
print('%s的年龄是:%d' % (name, age))  # chris的年龄是:23

info = (name, age)
print('%s的年龄是:%d' % info)  # chris的年龄是:23

# 元组中的数据不可以被修改，保护数据的安全
