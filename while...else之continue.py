i = 1
while i < 6:
    if i == 3:
        print("这遍不真诚")
        i = i + 1    # 注意用continue一定要改变计数器
        continue
    print("媳妇我错了")
    i = i + 1
else:
    print("媳妇原谅我了")
