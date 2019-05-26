import datetime

def betweenDays(startDate, endDate):
  start = datetime.datetime.strptime(startDate, '%Y-%m-%d')
  end = datetime.datetime.strptime(endDate, '%Y-%m-%d')
  delta = end - start
  for i in range(delta.days + 1):
    day_ = start + datetime.timedelta(days=i)
    print(day_.strftime('%Y-%m-%d'))

betweenDays('2019-02-27','2019-03-02')