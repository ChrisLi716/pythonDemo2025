# for 临时变量 in 可迭代对象
#     循环体

s = 'this is a python for demo'
for i in s:
    print(i)

# range() 用来记录循环次数，相当于一个计数器
# range(start,stop,step)
# 取1到5的5个数
'''
1
2
3
4
5
'''
for i in range(1, 6):
    print(i)

'''
0
1
2
3
4
'''
for i in range(5):
    print(i)

result = 0
for i in range(1, 101):
    result += i
print(f'1...100的求各结果：{result}')  # 5050

for i in range(1, 12):
    if i == 3:
        break
    print(f"current value:{i}")

for i in range(1, 12):
    if i == 3:
        print(f"current value:{i}, don't print")
        continue
    print(f"current value:{i}")
