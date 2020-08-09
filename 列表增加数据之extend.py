"""
1.extend追加的数据如果是一个序列，会将序列里的数据拆开并逐一追加到结尾
2.如果是列表，则去掉【】再追加到结尾
"""

name_list = ['tom', 'lily', 'jim']

# name_list.extend("xiaoming")
name_list.extend(["xiaoming", "xiaohong"])
print(name_list)
