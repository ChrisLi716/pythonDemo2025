# 字典
# 格式： 字典名={key1:value1, k2:value2...}

dic = {'name': 'chris', 'age': 18}
print(type(dic))  # <class 'dict'>
print(dic)  # {'name': 'chris', 'age': 18}

# 字典中的键具有唯一性，但是值可以重复，键名重复时前面的值会被后面的覆盖掉
dic = {'name': 'chris', 'age': 18, 'name': 'john'}
print(dic)  # {'name': 'john', 'age': 18}

# 查询
# 变更名[键名]
dic = {'name': 'chris', 'age': 18}
print(dic['name'])  # chris
# print(dic['address'])  # KeyError: 'address', 键名不存在时会报错

# 变更名.get(键名)
print(dic.get('name'))  # chris
print(dic.get('address'))  # None, 键名不存在时不会报错，而是返回None
print(dic.get('address', 'not exist'))  # not exist, 键名不存在时不会报错，而是返回None, 可以指定返回值

# 修改
dic = {'name': 'chris', 'age': 18}
dic['age'] = 23
print(dic)  # {'name': 'chris', 'age': 23}
dic['address'] = 'cn'
print(dic)  # {'name': 'chris', 'age': 23, 'address': 'cn'}, 键名存在则修改， 不存在则新增

# 删除 del, clear, pop
dic = {'name': 'chris', 'age': 18}
# del dic
# del dic['age'] # NameError: name 'dic' is not defined, 字典已被删除后再操作就报错

del dic['age']
print(dic)  # {'name': 'chris'}
# del dic['address']  # KeyError: 'address', 字典键名不存在，删除时报错

# clear() 清空字典里面的所有东西，但是保留了字典的定义
dic.clear()  # {}
print(dic)
dic['phone'] = 121345788  # {'phone': 121345788}
print(dic)

# pop() 删除指定键值对，键不存在就会报错
dic = {'name': 'chris', 'age': 18, 'address': 'us'}
dic.pop('name')  # {'age': 18, 'address': 'us'}
print(dic)

# dic.pop('phone')  # KeyError: 'phone'
dic.popitem()  # KeyError: 'phone'
print(dic)  # {'age': 18}, 3.7之前的版本随机删除一个键值对，3.7之后的版本删除最后一个键值对

# len()求长度
dic = {'name': 'chris', 'age': 18, 'address': 'us'}
print(len(dic))  # 3

#  keys() 返回安字典里面包装的所有键名
dic = {'name': 'chris', 'age': 18, 'address': 'us'}
print(dic.keys())  # dict_keys(['name', 'age', 'address'])

for i in dic.keys():
    print(i)

#  values() 返回安字典里面包含的所有值
print(dic.values())
for i in dic.values():
    print(i)

# item() 返回字典里面的键值对，以元组的形式返回
'''
('name', 'chris')
('age', 18)
('address', 'us')
'''
for item in dic.items():
    print(item)

# 字典的应用场景： 可以用字典存储对象
