import datetime

t1 = '2017-11-18 17:05:31'
t2 = '2013-11-18 17:05:31'

t1_datetime = datetime.datetime.strptime(t1, '%Y-%m-%d %H:%M:%S')
t2_datetime = datetime.datetime.strptime(t2, '%Y-%m-%d %H:%M:%S')
print('相差', (t1_datetime - t2_datetime).days, '天')
print('相差', (t1_datetime - t2_datetime).total_seconds(), '秒')

n = int(input())
print(datetime.date.today() + datetime.timedelta(days=n))
