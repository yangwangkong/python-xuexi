"""
1.准备做加法1-100且增量为1的数据
2.准备一个变量保存将来的结果
3.循环做加法运算
4.打印结果
5.验证结果
"""

i = 1
result = 0
while i <= 100:
    result = result + i
    i = i + 1
    # print(result)
print(result)
