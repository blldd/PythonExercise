# -*- coding: utf-8 -*-


#
# def prepare():
#     pass
#
#
#
#
# def hello():
#     pass
#     # print("hello")
#
#
# hello()
#
#
# str = "hello\n\t"
# for i in range(10):
#     print(i)


"""
函数都带(),里面有参数
range()

[]  list
[  ,  ,  ,  ,]
()  tuple
{}  dict 字典

()  set  堆

小明  7 8 7

"""


def test():
    list1 = range(10)
    list = range(10)
    return (list, list1)


(l, l1) = test()

if __name__ == '__main__':
    tuple = ()
    list1 = range(10)
    print(list1)
    foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
    # print(list(map(lambda x:2**x, foo)))
    square = [2 ** x for x in foo]  # pythonic
    print(square)

    print foo[0]
    foo[0] = 4
    print(foo[0])
    foo_tuple = (2, 18, 9, 22, 17, 24, 8, 12, 27)
    print(foo_tuple)
    # foo_tuple[0] = 4
    # print(foo_tuple[0])

    print foo[2:6]
    print foo[:6]
    print foo[2:]
    print foo[:]
    print foo[2:6]

    square = [2 ** x for x in foo if x > 20]  # pythonic
    print(square)
    print max(square)
    foo = sorted(foo, reverse=True)
    print(foo)
    print(foo[len(foo) - 2:])
    print(foo[-2:])
    print(foo[:-2])
    print(foo[2::2])
    print(foo[::2])

    print(foo)
    "27 24 22"
    # print str(foo)
    # for i in range(len(foo)):
    #     print(foo[i])
    for x in foo:
        print(x)
    s = ""
    for x in foo:
        s += str(x) + " "
    print(s)

    print(" ".join([str(x) for x in foo]))
    print(" ".join(map(str, foo)))

    li = [3234, "3423", "jkjfsld"]
    print(li)
    print(" ".join(map(str, li)))

    # 键值对  key-value pair
    stuff = {"name": 'Zed', 'age': 36, 'height': 6 * 12 + 2}
    print("my name is " + stuff["name"])
    for key in stuff:
        print(key)
    for value in stuff.values():
        print(value)
    for key in stuff:
        print(stuff.get(key))
        print(stuff[key])

    #
    # f = range()
    # test = f(10)
    # print(test)


# from ex48 import lexicon
# print lexicon.scan("go north")
