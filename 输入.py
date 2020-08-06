'''
1.书写input
    input(’提示信息‘)

2.观察特点
    2.1 遇到input，等待用户输入
    2.2 接受input存变量
    2.3 input接受到的数据的类型都是字符串
'''

password = input("请输入密码：")
print(f"您输入的密码是{password}")
# 检测类型--type
print(type(password))
