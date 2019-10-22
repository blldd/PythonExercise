# -*- coding: utf-8 -*-
# @ Dedong Li
# @ 2019-10-18

"""Example Google style docstrings."""

import pickle


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'name:{} age:{}'.format(self.name, self.age)


xiaoming = Person('xiaoming', 18)

# 序列化：将对象转换为bytes类型
s = pickle.dumps(xiaoming)
print(s)

# 反序列化：将bytes转换为对象
xm = pickle.loads(s)
print(xm, type(xm))

# 保存到文件
fp = open('data.txt', 'wb')

# s = pickle.dumps(xiaoming)
# fp.write(s)

# 等价于上面两步
pickle.dump(xiaoming, fp)
fp.close()

# 从文件中读取
fp = open('data.txt', 'rb')

# s = fp.read()
# xm = pickle.loads(s)
# 等价于上面两步
xm = pickle.load(fp)

print(xm)
fp.close()
