"""
1.准备数据
    1.1 8位老师的数据和3个办公室的数据
    1.2 用列表嵌套和列表存储
2.分配老师到办公室
    2.1 随机模块
    2.2 办公室列表追加老师名字
3.验证是否分配成功
    3.1 打印每个办公室的详细信息：每个办公室人数与对应老师名字
"""

import random

teacher = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
office = [[], [], []]

# 分配老师到办公室 -- 遍历老师列表数据
for name in teacher:
    # 列表追加数据
    i = random.randint(0, 2)
    office[i].append(name)
print(office)

# 验证
for j in office:
    print(j)
    print(f'办公室人数是{len(j)}')
