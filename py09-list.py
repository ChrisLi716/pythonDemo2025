# 处理一组有序项目的数据结构, 元素间的数据类型可以不相同
# 列表名=[1,'2',False, "Hello"]
lst = [1, 2, 3, False, "Chris"]
print(lst, type(lst))  # [1, 2, 3, False, 'Chris'] <class 'list'>
print(lst[0])  # 1
print(lst[0:4])  # [1, 2, 3, False], 包前不包后q

# 列表是可以迭代的，可以for循环遍历取值
for i in lst:
    print(i)

# 列表常用操作
# 1 添加元素  append, extend, insert
li = [1, 2, 3]
li.append(4)  # 在后面做为一个整体添加
print(li)

li.extend("chris")  # [1, 2, 3, 4]
# li.extend(5)  # TypeError: 'int' object is not iterable， extend里面要是可迭代对象，不然后报错
print(li)  # [1, 2, 3, 4, 'c', 'h', 'r', 'i', 's'] 分散添加

li.insert(4, "hello")
print(li)  # [1, 2, 3, 4, 'hello', 'c', 'h', 'r', 'i', 's'], 在指定位置添加元素，原有元素后移

# 2 修改元素
li = [1, 2, 3]
li[1] = 'a'
print(li)  # [1, 'a', 3]

# 3 查询
#  in 判断指定元素是否存在列表中，存在返回True 不存在返回False
#  not in 判断指定元素是否不存在列表中，不存在返回True 存在返回False

li = [1, 2, 3, 5, 6]
print(2 in li)  # True
print(4 in li)  # False
print(7 not in li)  # True

'''
alias = ['chris', 'john', 'Alex', 'Peter']
while True:
    a = input("pls input your alia:")
    if a not in alias:
        print(f"{a} is your alia")
        alias.append(a);
        break
    else:
        print(f"{a} has been used, pls input available alia")

print(alias)
'''

# index 返回指定元素所在位置在下标， 如是查找的数据不存在就会报错
# count 统计指定数据在当前列表中出现的次数
li = [1, 2, 3, 5, 6, 2, 5, 4, 6, 8, 7, 5]
inx = li.index(1)
print(inx)  # 0
# li.index('1') # ValueError: '1' is not in list
print(li.count(5))  # 3

# 4 删除元素 del, pop, remove

li = [1, 2, 3, 5, 6, '1', 'a']
# del li
# del li[2] # NameError: name 'li' is not defined, 因为整个列表已经被删除了， 所以不能再删除其中的元素
# print(li)  # NameError: name 'li' is not defined，  因为整个列表已经被删除了， 所以不能再删除其中的元素

del li[2]
print(li)

li = [1, 2, 3, 4, 5, 6]
li.pop()
print(li)  # [1, 2, 3, 4, 5], pop()默认删除最后一个元素

li.pop(2)
print(li)  # [1, 2, 4, 5] 指定下标删除指定位置的元素
# li.pop(7)  # 如果下标超出范围会报错 IndexError: pop index out of range

li = [1, 2, 3, 4, 5, 6, 5]
li.remove(3)  # [1, 2, 4, 5, 6, 5], 根据指定元素删除
print(li)

# li.remove(122)  # 如果被移除的元素不存在则会报错 tqbValueError: list.remove(x): x not in list
li.remove(5)
print(li)  # [1, 2, 4, 6, 5], 只会删除第一个5

# 5 排序
li = [1, 4, 2, 5, 2, 3, 5]
li.sort()
print(li)  # [1, 2, 2, 3, 4, 5, 5] 按从小到大的顺序排序

li.reverse()
print(li)  # [5, 5, 4, 3, 2, 2, 1] ,将列表元素倒转

li.sort()
li.reverse()
print(li)  # [5, 5, 4, 3, 2, 2, 1], 先从小到大排序再将元素倒转就可以实现从大小到排序

# 6 列表推导式
# 格式1， [表达式 for 变量 in 列表]

li = []
for i in range(10):
    li.append(i)
print(li)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

li2 = []
[li2.append(i) for i in range(10)]
print(li2)

# 格式1， [表达式 for 变量 in 列表 if 条件]
li = []
for i in range(10):
    if i % 2 == 1:
        li.append(i)
print(li)  # [1, 3, 5, 7, 9]

li2 = []
[li2.append(i) for i in range(10) if i % 2 == 1]
print(li2)  # [1, 3, 5, 7, 9]

# 7 列表嵌套
li = [1, 2, 3, [4, 5, 6]]
print(li[3])  # [4, 5, 6], 取出里面的列表
print(li[3][2])  # 6, 取出里面的列表的第2个元素
