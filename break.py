"""
吃5个苹果，吃到第三个吃饱了的代码实现
"""

i = 1
while i <= 5:
    if i == 4:
        print("吃饱了")
        break
    print(f"正在吃第{i}个苹果")
    i = i + 1
