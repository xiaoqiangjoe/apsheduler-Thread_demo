from threading import Thread
import datetime
import time
import db


def db1():
    db.db_in()

if __name__ == '__main__':
    while True:
        time.sleep(5)
        t = Thread(target=db1)
        t.start()
