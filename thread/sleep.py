import threading
import time
import datetime


def job():
    for _ in range(5):
        print(datetime.datetime.now().strftime('%H:%M:%S'), 'alive')
        time.sleep(5)


t = threading.Thread(target=job)

t.start()
