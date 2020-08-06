"""
前提：使用条件语句，先从1开始判断是否为偶数再相加
1.准备要累加的数字  开始1  结束100
2.准备保存结果的变量
3.循环做加法运算
4.输出结果
5.验证结果
"""

i = 1
result = 0
while i <= 100:
    if i % 2 == 0:
        result = result + i
        i = i + 1
    else:
        i = i + 1
print(result)
