a = 12

while a >= 1:
    print(a)
    a -= 1

i = 1
result = 0
while i <= 100:
    result += i
    i += 1

print(f'1...100的求各结果：{result}')  # 5050

# while嵌套
m = 1
while m <= 3:
    print(f'外循环第{m}次')
    n = 1
    while n <= 5:
        print(f'\t内循环第{n}次')
        n += 1
    m += 1
