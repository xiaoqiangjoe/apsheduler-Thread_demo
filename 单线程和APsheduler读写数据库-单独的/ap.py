from apscheduler.schedulers.blocking import BlockingScheduler
import db

def job1():
    ret = db.db_read()
    print('在ap中',ret)


scheduler = BlockingScheduler()
scheduler.add_job(job1, 'interval', seconds=5)  # 每隔5秒执行一次
scheduler.start()
