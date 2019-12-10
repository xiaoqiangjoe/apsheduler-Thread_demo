# 导入pymysql模块
import pymysql
import time
import random
# 连接database
conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='apsheduler')


def db_in():
    conn.ping(reconnect=True)
        # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()
    time.sleep(5)
    wendu = random.randint(0,50)
    shidu = random.randint(0,80)

    sql = "INSERT INTO weather(wendu, shidu) VALUES ({},{});".format(wendu, shidu)
    print(sql)
    # 执行SQL语句
    cursor.execute(sql)
    # 提交事务
    conn.commit()


def db_read():
    conn.ping(reconnect=True)
    cursor = conn.cursor()

    # 查询数据的SQL语句
    sql = "SELECT wendu, shidu from weather ORDER BY id DESC LIMIT 0,5;"

    # 执行SQL语句
    cursor.execute(sql)
    # 获取单条查询数据
    ret = cursor.fetchall()
    print('ret',ret)
    cursor.close()
    conn.close()
    # 打印下查询结果
    return ret
