# -*- coding:UTF-8 -*-
"""
Go Card

Creating account. Input initial balance: 100
? r 3.50
? r 10.90
?b
Balance = $85.60
? t 20
? x gghhg
Bad command.
?t
Bad command.
?q

Statement:
event ...

"""


class GoCard:
    def __init__(self, startBal):                                       # 类初始化，每调用一次类，就会根据传进来的初始值，生成一个account对象
        self._balance = startBal
        self._record = [startBal]

    def trip(self, amount):
        self._balance -= amount
        self._record.append(-amount)

    def topUp(self, amount):
        self._balance += amount
        self._record.append(amount)

    def getBalance(self):
        return self._balance

    def printStatement(self):
        print "Statement:"
        print "{:15s} {:>11s} {:>11s}".format("event", "amount ($)", "balance ($)")
        balance = self._record[0]
        print "{:15s} {:11s} {:11.2f}".format("Initial balance", "", balance)
        for r in self._record[1:]:
            balance += r
            if r < 0.0:
                print "{:15s} {:11.2f} {:11.2f}".format("Ride", -r, balance)
            else:
                print "{:15s} {:11.2f} {:11.2f}".format("Top up", r, balance)
        print "{:15s} {:11s} {:11.2f}".format("Final balance", "", balance)

# 获取到账户初始值
amount = float(raw_input("Creating account. Input initial balance:"))
# 通过 GoCard（类） 生成一个 accout（对象），默认调用类中的__init__方法。
# 从此 account对象 就拥有了GoCard类中所有的方法（即类中def后的都可以通过account.*来调用）
account = GoCard(amount)

command = raw_input("? ")

while command.strip() != "q":
    ws = command.split()
    if len(ws) == 2 and ws[0] == 'r':
        try:
            dollars = float(ws[1])
            account.trip(dollars)                               # 调用 account.trip()
        except:
            print "Bad command."
    elif len(ws) == 2 and ws[0] == 't':
        try:
            dollars = float(ws[1])
            account.topUp(dollars)                              # 调用 account.topUp()
        except:
            print "Bad command."
    elif len(ws) == 1 and ws[0] == 'b':
        print "Balance = ${:.2f}".format(account.getBalance())  # 调用 account.getBalance()
    else:
        print "Bad command."
    command = raw_input("? ")

# 调用 account.printStatement()， 里面用到了很多符号，需要你去学习一下format函数，例如>是指右对齐
# 3.3不用此函数
account.printStatement()
