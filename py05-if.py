age = 17
if age < 18:
    print("未成年人")
else:
    print("成年人")

score = 12
if score == 100:
    print("A")
elif 90 <= score < 100:
    print("B")
elif 80 <= score < 90:
    print("C")
else:
    print("D")

# if嵌套
ticket = True
temperature = 36.5

if ticket:
    print("有票可以进站")
    if 36.3 <= temperature <= 37.2:
        print("体温正常可以上车")
    else:
        print("体温不正常，不能上车")
else:
    print("没有票可以进站")
