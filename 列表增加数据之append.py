"""
1.列表是可变的
2.append -- 追加数据的时候，如果数据是列表形式，它会追加到列表结尾
"""

name_list = ['tom', 'lily', 'jim']
# name_list.append("xiaoming")
name_list.append([11, 22])
print(name_list)
