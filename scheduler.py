from apscheduler.schedulers.blocking import BlockingScheduler
from rq import Queue
from utils import retrieve_current_price
from worker import conn

endpoint = 'https://api.coindesk.com/v1/bpi/currentprice/USD.json'

scheduler = BlockingScheduler()

q = Queue(connection=conn)


@scheduler.scheduled_job('interval', minutes=5)
def retrieve_current_price_job():
    q.enqueue(retrieve_current_price, endpoint)


scheduler.start()
