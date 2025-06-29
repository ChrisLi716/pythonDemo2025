# 集合
# 格式 s={1,2,3,'a', True, False, None}
# 1. 集合是无序的，里面的元素是唯一的
# 2. 可以用于元组或者列表去重
# 3. 集合的元素可以是不同的数据类型
# 4. 集合和元组一样，只支持查询不支持修改

s = {1, 2, 3, 'a', True, False, None}
print(type(s))  # <class 'set'>

# 定义空集合
s = set()

# 集合是无序的
s1 = {1, 2, 3, 'a', True, False, None}
print(s1)  # {'a', 1, 2, 3, False, None}， 每次运行的结果都是不一样的

s2 = {1, 2, 3, 5, 6}
print(s2)  # {1, 2, 3, 5, 6}， 数字每次运行结果都是一样的

# 集合无序的实现方式涉及hash表
# 字符串每次运行的hash值不同，在hash表中的位置也就不同，这样就实现了集合的无序性
'''
-6417635280626746124
-1231411697408350987
3699728425578917391
5781419579719735714
8523634356119646545
'''
print(hash('1'), hash('2'), hash('3'), hash('4'), hash('5'), sep='\n')

# 整形的hash值是它本身, 在hash表中的位置不会发生变化，所以顺序也不会改变
'''
1
2
1614090106449586179
1152921504606846980
5
'''
print(hash(1), hash(2), hash(3.7), hash(4.5), hash(5), sep='\n')

# 集合具有唯一性，可以去重
s3 = {1, 2, 3, 5, 2, 4, 3, 6}
print(s3)  # {1, 2, 3, 4, 5, 6}

# 添加元素 add, update
s3 = {1, 2, 3, 5, 2, 4, 3, 6}
s3.add('d')
s3.add(3)  # 如果添加的元素在原集合中已经存在，则不进行任何操作
print(s3)  # {1, 2, 3, 4, 5, 6, 'd'}

s4 = {1, 2, 3}
# update把传入的可迭代对象拆分，一个个放进集合
s4.update('abc')  # 添加字符串中的每个元素
s4.update([7, 8, 9])  # 添加列表中的每个元素
s4.update((10, 11, 12))  # 添加元组中的每个元素
s4.update({'name': 'chris', 'age': 18})  # 添加字典中的每个key元素
print(s4)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 'd', 'name', 'c', 'a', 'age', 'b'}

# 删除元素 remove(), pop(), discard()
# remove() 如果集合中有则删除没有就报错
s5 = {1, 2, 3}
s5.remove(2)
# s5.remove('d') # KeyError: 'd'
print(s5)  # {1, 3}

# pop() 删除对集合无序排列后左边的第一个元素
s6 = {'a', 1, 2, 3, 'b'}
s6.pop()
print(s6)  # {2, 3, 'a', 'b'}

# discard() 选择要删除的元素，有则删除没有也不会报错
s6 = {'a', 1, 2, 3, 'b'}
s6.discard('a')
s6.discard('c')
print(s6)  # {1, 2, 3, 'b'}

# 交集& 与 盖并集|
a = {1, 2, 3, 'b'}
b = {'a', 2, 3, }
print(a & b)  # 交集{2, 3}
print(a | b)  # 并集{1, 2, 3, 'b', 'a'}
