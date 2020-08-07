
mystr = 'hello world and itcast and itgdut and python'

# 用find查找（从左侧查找）
# print(mystr.find('and'))    # 12
# print(mystr.find('and', 15, 30))    # 23
# print(mystr.find('ands'))     # -1,ands字串不存在


# index查找（从左侧查找）
# print(mystr.index('and'))    # 12
# print(mystr.index('and', 15, 30))    # 23
# print(mystr.index('ands'))   # 报错,查找不到这个字串

# 用count数次数
print(mystr.count('and', 15, 30))
print(mystr.count('and'))
print(mystr.count('ands'))      # 不报错

# rfind查找从右侧查找
# rindex查找从右侧查找
