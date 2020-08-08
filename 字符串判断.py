mystr = 'Hello world and itGdut and python'

# isalpha -- 判断字符串是否全是字母组成
print(mystr.isalpha())
# isdigit -- 判断字符串是否全是数字
print(mystr.isdigit())
mystr1 = '123456'
print(mystr1.isdigit())
# isalnum -- 数字或字母或数字字母组合（不能有空格）
print(mystr.isalnum())
print(mystr1.isalnum())
mystr2 = 'abc123'
print(mystr2.isalnum())


# isspace -- 都是空白才是true
print(mystr.isspace())
mystr3 = '     '
print(mystr3.isspace())
