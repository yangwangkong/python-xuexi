# 三角形星星：每行的星星个数与行号相等，所以i和j要有联动的关系
j = 0
while j < 5:
    # 一行星星开始
    i = 0
    while i <= j:
        print("*", end='')
        i = i + 1
    # 一行星星结束，换行显示下一行
    print()  # 借助空的print，利用print默认结束符换行
    j = j + 1
