import arrow

day = arrow.now().format('DDMMYY')
print(day)

time = arrow.now().format('HHMM')
print(time)