# -*- coding: utf-8 -*-
# @ Dedong Li
# @ 2019-10-18

"""Example Google style docstrings."""

import time
import datetime
import hashlib
import shelve

# 模拟一个网站登录，新用户先进行注册再登录，
# 旧用户登录判断登录的时间，离上一次登录时间超过多长时间的就再也不能登录了。
# 只适用于一些开放的临时登录的场景？

# 测试时设置登录超时的时间为6分钟，实际应用可以设时间久一点
LOGIN_TIME_OUT = 0.60

# 设置一个临时db，且允许拷贝写回
db = shelve.open('user_shelve.db', writeback=True)

#　新用户登录函数,后面测试后发现其实就是相当于新注册一个用户！
def newuser():
    prompt = "login desired: " # prompt,提示
    while True:
        name = input(prompt).strip()
        if name in db:
            prompt = "name taken, try another: " #  用户己存在，请重新输入
            continue
        elif len(name) == 0:
            prompt = "name should not be empty, try another: "  # 用户名不应该是空的，请重新输入
            continue
        else:
            break
    pwd = input("password: ").strip()
    db[name] = {"password": md5_digest(pwd), "last_login_time": time.time()}

# 判断用户有没有已存在登录及记录上一次登录时间的函数（现有用户）
def olduser():
    name = input("login: ").strip()
    pwd = input("password: ").strip()
    try:
        password = db.get(name).get('password')
        # 捕获一个异常，试图访问一个对象没有的属性，也就是处理用户输入不存在的用户时
    except AttributeError:
        print("\033[1;31;40mUsername '%s' doesn't existed\033[0m" % name)
        # 提示用户不存在
        return
    if md5_digest(pwd) == password:
        login_time = time.time()   # 当前登录时间
        print(login_time)
        last_login_time = db.get(name).get('last_login_time') # 上一次登录时间
        print(last_login_time)
        if login_time - last_login_time < LOGIN_TIME_OUT: # 如果登录没有超时
            print("\033[1;31;40mYou already logged in at: <%s>\033[0m" % datetime.datetime.fromtimestamp(
                last_login_time).isoformat()) # 显示你准备登录的时间
        db[name]['last_login_time'] = login_time # 写入登录时间到db
        print("\033[1;32;40mwelcome back\033[0m", name) # 显示欢迎回来
    else:
        print("\033[1;31;40mlogin incorrect\033[0m") # 否则显示登录失败

#　md5摘要加密传输进来的明文密码
def md5_digest(plain_pass):
    md5 = hashlib.md5()
    md5.update(plain_pass.encode('utf-8'))
    return md5.hexdigest()

# 菜单
def showmenu():
    # 下面菜单分别是新用户登录，当前用户登录，退出
    prompt = """
(N)ew User Login
(E)xisting User Login
(Q)uit
Enter choice: """
    done = False #　完成 默认值false
    while not done:
        chosen = False # 选择 默认值false
        while not chosen:
            try:
                choice = input(prompt).strip()[0].lower()
                # 捕获异常选择直接变成选q退出程序
            except (EOFError, KeyboardInterrupt):
                choice = "q"
            print("\nYou picked: [%s]" % choice) # 提示你的选择是什么
            if choice not in "neq":
                print("invalid option, try again") # 当输入的不为neq时，提示输入有误请重新输入
            else:
                chosen = True # 选择 为真，中断循环

        if choice == "q": done = True # 选择为q,退出，中断循环
        if choice == "n": newuser() # 选择为n，执行newuser()函数
        if choice == "e": olduser() # 选择为e，执行olduser()函数
    db.close() # 关闭db文件句柄

# 执行主程序
showmenu()

