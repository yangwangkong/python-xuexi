name_list = ['tom', 'lily', 'jim']

name = input("请输入一个账户名：\n")
if name in name_list:
    print(f"您输入的名字是{name}，用户名已存在")
else:
    print(f"您输入的名字是{name}，可以注册")
