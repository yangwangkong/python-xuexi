name_list = ['tom', 'lily', 'jim']

# 1.del  --  可以删除指定下标的数据或者整个列表
# del name_list
# del name_list[0]

# 2.pop -- 删除指定下标的数据，不写默认删除最后一个数据，且会返回删除的数据的值
# del_name = name_list.pop(2)
# del_name = name_list.pop(1)
# print(del_name)

# 3.remove(数据)
# name_list.remove('jim')

# 4.clear -- 清空
name_list.clear()
print(name_list)
