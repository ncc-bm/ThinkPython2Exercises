import time

current_time = time.time()
print('Epoh time', current_time)
seconds_in_hour = 3600
seconds_in_day = seconds_in_hour * 24
print('Seconds in a day =', seconds_in_day)

days_since_epoch = current_time // seconds_in_day
print('Days since the epoch =', int(days_since_epoch))
print('Years since the epoch = ', int(days_since_epoch//365))

hour_time = current_time - (days_since_epoch * seconds_in_day)
print('Seconds to calculate current time =', int(hour_time))

hour = int(hour_time // seconds_in_hour)
print('Current time Hours =', hour+5)

minute_time = int(hour_time - (hour * seconds_in_hour))
print('Seconds to calculate current minutes =', minute_time)
minute = int(minute_time // 60)
print('Current minutes=', minute)

second_time = int(minute_time - (minute * 60))
print('Current seconds=', second_time)


print('Result:')
print('Days since the epoch: ', int(days_since_epoch), ' days, current time ', hour,':', minute, ':', second_time, sep='' )