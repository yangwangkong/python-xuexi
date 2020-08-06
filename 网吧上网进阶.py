"""
1.用户输入
2.保存用户输入的年龄
3.if
***** 注意一个点：input接受到的数据是str类型
"""

age = int(input("请输入您的年龄："))
if age >= 18:
    print(f"您的年龄是{age},已经成年，可以上网")
else:
    print(f"您的年龄是{age}，小朋友回家写作业去")
