# 代码顶格写， 不要缩进， 不然后报 IndentationError: unexpected indent
# python中的字符都是英文模式下的

# hello my first python code
print("hello my first python code")

# 单选注释用#， ctrl+/
# 多行注释,用三个单引号或者三个双引号
'''
sep:用来设置间隔符
Hello
I'm chris
how are you today?
'''
print('Hello', 'I\'m chris', 'how are you today?', sep='|')

# end：用来设置换行符，默认为换行符\n,可以换成其它字符串
# Hello,I'm chris,how are you today?;hello, I'm john ,nice to meet you
print('Hello', 'I\'m chris', 'how are you today?', sep=',', end=";")
print('hello, I\'m john ,nice to meet you')
