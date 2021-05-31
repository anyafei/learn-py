#!/usr/bin/python3

# 保留关键字
import keyword
keyword.kwlist

# 这是注释符号
print("Hello, Python!")

# 行与缩进 缩进不一致会报错
if True:
    print("Answer")
    print("True")
else:
    print("Answer")
    print("False")

# 多行语句
total = 'item_one' + \
        'item_two' + \
        'item_three'

total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']

# 字符串
str = 'Runoob'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始后的所有字符
print(str[1:5:2])  # 输出从第二个开始到第五个且每隔两个的字符
print(str * 2)  # 输出字符串两次
print(str + '你好')  # 连接字符串

print('------------------------------')

print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""
x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print('---------')
# 不换行输出
print(x, end=" ")
print(y, end=" ")
print()


# 在 python 用 import 或者 from...import 来导入相应的模块。
# 将整个模块(somemodule)导入，格式为： import somemodule
# 从某个模块中导入某个函数,格式为： from somemodule import somefunction
# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
# 将某个模块中的全部函数导入，格式为： from somemodule import *