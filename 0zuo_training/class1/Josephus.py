# -*- coding:UTF-8 -*-


class Node:
    def __init__(self, data):
        self.value = data
        self.next = None


def josephus(head, m):
    """
    :return:
    """
    if head == None or head.next.value == head.value or m < 1:
        return head
    last = head
    while last.next.value != head.value:
        last = last.next
    count = 0
    while head.value != last.value:
        count += 1
        if count == m:
            last.next = head.next
            count = 0
        else:
            last = last.next
        head = last.next
    return head


def getLive(i, m):
    if i == 1:
        return 1
    return (getLive(i - 1, m) + m - 1) % i + 1


def josephus1(head, m):
    """
    """
    if head == None or head.next.value == head.value or m < 1:
        return head
    cur = head.next
    tmp = 1
    while cur.value != head.value:
        tmp += 1
        cur = cur.next
    tmp = getLive(tmp, m)
    tmp -= 1
    while tmp != 0:
        head = head.next
        tmp -= 1
    head.next = head
    return head



def printCircularList(head):
    if head == None:
        return
    print("Circular List: " + str(head.value) + " ", end="")
    cur = head.next
    while cur.value != head.value:
        print(str(cur.value) + " ", end="")
        cur = cur.next
    print("-> " + str(head.value))


if __name__ == '__main__':
    """
    某公司招聘，有n个人入围，HR在黑板上依次写下m个正整数A1、A2、......、Am，然后让这n个人围成一个 圈，
	并按照顺时针顺序为他们编号0、1、2、......、n-1。
	录取规则是: 第一轮从0号的人开始，取用黑板上的第1个数字，也就是A1 黑板上的数字按次序循环取用，
	即如果某轮用了第m个，则下一轮需要用第1个;如果某轮用到第k个，
	则 下轮需要用第k+1个(k<m) 每一轮按照黑板上的次序取用到一个数字Ax，
	淘汰掉从当前轮到的人开始按照顺时针顺序数到的第Ax个 人，
	下一轮开始时轮到的人即为被淘汰掉的人的顺时针顺序下一个人 被淘汰的人直接回家，所以不会被后续轮次计数时数到
	经过n-1轮后，剩下的最后1人被录取 所以最后被录取的人的编号与(n，m，A1，A2，......，Am)相关。
	输入描述:
	第一行是一个正整数N，表示有N组参数 从第二行开始，每行有若干个正整数，依次存放n、m、A1、......、Am，一共有N行，也就是上面的N组参 数。
	输出描述:
	输出有N行，每行对应相应的那组参数确定的录取之人的编号示例1:
	输入
	1
	4231
	输出
	1
	"""
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    head1.next.next.next.next = Node(5)
    head1.next.next.next.next.next = head1
    printCircularList(head1)
    josephus1(head1, 3)
    printCircularList(head1)
