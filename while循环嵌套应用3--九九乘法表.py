"""
多行多个乘法表达式
1.打印一个乘法表达式：X * X = X*X
2.一行打印多个乘法表达式：行号与一行表达式个数相等 --- 循环一个表达式
3.打印多行表达式：循环打印一行表达式--换行

****一行表达式个数与行号数相等
"""
j = 1
while j <= 9:
    # 一行的表达式
    i = 1
    # i要和j有联动关系********
    while i <= j:
        print(f"{i} * {j} = {i * j}", end='\t')
        i = i + 1
    # 一行表达式结束
    print()
    j = j + 1
