str1 = "itGDUT"
for i in str1:
    if i == 'G':
        print("不打印G")
        # break退出循环
        break
        # continue退出当次循环
        # continue
    print(i)
else:
    print("循环正常结束后的代码")
