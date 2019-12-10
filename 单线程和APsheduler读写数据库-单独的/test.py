import time


while True:
    time.sleep(1)
    username = "Alex" + str(time.time())
    age = 80
    sql = "UPDATE USER1 SET age={} WHERE name={};".format(username,age)

    print(sql)