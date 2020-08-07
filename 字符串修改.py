
mystr = 'hello world and itcast and itgdut and python'

# replace 不会对原有字符串进行修改，需要新变量储存
# 字符串数据是不可变类型的数据
# new_str = mystr.replace('and', 'he')
# new_str = mystr.replace('and', 'he', 1)
new_str = mystr.replace('and', 'he', 10)
# 如果替换次数超出子串出现次数，则替换所有子串
print(new_str)

# split -- 返回一个列表，用作分割,会丢失分割字符
# list1 = mystr.split("and")
list1 = mystr.split("and", 2)
print(list1)

# join -- 合并字符串
mylist = ['aa', 'bb', 'cc']
new_list = '...'.join(mylist)
print(new_list)

