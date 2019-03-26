# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The test_oracle file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""
import re
from time import timezone

import cx_Oracle
import os

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
from datetime import datetime
from pytz import utc
from pytz import timezone

cst_tz = timezone('Asia/Shanghai')
utc_tz = timezone('UTC')
utcnow = datetime.utcnow()
print(utcnow)
utcnow = utcnow.replace(tzinfo=utc_tz)
china = utcnow.astimezone(cst_tz)
print(china)

now = datetime.utcnow().replace(tzinfo=utc_tz).astimezone(cst_tz)
print(now)
# now.fromtimestamp()

def table_exists(cursor,table_name):        #这个函数用来判断表是否存在
    stmt = "select Table_name from user_tables"
    cursor.execute(stmt)
    tables = cursor.fetchall()
    tables = {table[0].strip("'") for table in tables}
    if table_name.upper() in tables:
        return 1        #存在返回1
    else:
        return 0


db_pool = cx_Oracle.SessionPool(user='root',
                                password='passw0rd',
                                dsn='49.52.10.181:8021/xe',
                                min=2,
                                max=10,
                                increment=3)

connection = db_pool.acquire()
cursor = connection.cursor()

table_name = "my_test_table"

if not table_exists(cursor, table_name):
    print("not exist")
else:
    print("exist")

# 1. Drop table.
try:
    stmt = "drop table %s" % table_name
    print(stmt)
    cursor.execute(stmt)
except:
    pass

if not table_exists(cursor, table_name):
    print("not exist")
else:
    print("exist")

# 2. Create table.
stmt = "create table %s (id int, createTime DATE, confidence NUMBER(10,7), event_id varchar2(100), constraint TF_B_AIR_CONFIG_PK primary key(id))" % table_name
print(stmt)
cursor.execute(stmt)
#

# 3. Insert row.
stmt = "insert into %s(id, createTime, confidence, event_id) values (:id, :createTime, :confidence, :event_id)" % table_name
cursor.execute(stmt, id=1, createTime=china, confidence=0.987, event_id="153261")
cursor.execute(stmt, id=2, createTime=china, confidence=0.00001, event_id="1532616672395")
cursor.execute(stmt, id=3, createTime=china, confidence=123.9879234, event_id="1532616672395")
# cursor.execute(stmt, id=1, createTime=china, confidence=0.98723, event_id="15322361")
print(stmt)
print("Commit changes")
connection.commit()

# 4. Query row.
stmt = "select * from %s" % table_name
cursor.execute(stmt)
for id_, createTime_, confidence_, event_id_ in cursor.fetchall():
    print(id_, createTime_, confidence_, event_id_)

# 5. Update row.
stmt = "update %s set event_id = 'ok' where id = 1" % table_name
cursor.execute(stmt)

# 6. Delete row.
stmt = "delete %s where id = 3" % table_name
cursor.execute(stmt)

print("Commit changes")
connection.commit()

# 7. Query row.
stmt = "select * from %s" % table_name
cursor.execute(stmt)
for id_, createTime_, confidence_, event_id_ in cursor.fetchall():
    print(id_, createTime_, confidence_, event_id_)

cursor.close()
db_pool.release(connection)
