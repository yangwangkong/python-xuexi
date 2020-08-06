'''
1.准备数据
2.格式化符号输出数据
'''
age = 18
name = 'Yyr'
weight = 75.5
stu_id = 1

# 1.今年我的年龄是X岁
print("今年我的年龄是%d岁" % age)
# 2.我的名字是X
print("我的名字是%s" % name)
# 3.我的体重是X公斤
print("我的体重是%.2f公斤" % weight)
# 4.我的学号是X
print("我的学号是%d" % stu_id)
# 5.我的名字是X，今年X岁了
print("我的名字是%s，今年%d岁了" % (name, age))
# 6.我的名字是X，今年X岁了，体重X公斤，学号是X--%02d，表示输出的整数显示位数，不足以0补全，超出当前位数原样输出
print("我的名字是%s，今年%d岁了，体重%.2f公斤，学号是%03d" % (name, age, weight, stu_id))