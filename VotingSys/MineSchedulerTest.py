import requests
import datetime
import time
from apscheduler.schedulers.blocking import BlockingScheduler


def mine():
    #耗时5S
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    payload = {"sender": "aabcddeff", "recipient":"fuckyou", "amount":100}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    #r = requests.post("http://localhost:5001/transactions/new", json=payload, headers = headers)
    r = requests.get('http://localhost:5000/mine')
    print(r.json())    
    #time.sleep(10)

def dojob():
    #创建调度器：BlockingScheduler
    scheduler = BlockingScheduler()
    #添加任务,时间间隔2S
    scheduler.add_job(mine, 'interval', seconds=10, id='test_job1')

    scheduler.start()
	
dojob()




