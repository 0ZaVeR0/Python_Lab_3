from datetime import datetime

def nearest_time(times):
    time_diff = 9999999999
    for x in times:
        if min(abs(time_convert(x) - c_time()), abs(time_convert(x) + time_convert('24:00:00') - c_time())) < time_diff:
            time_diff = abs(time_convert(x) - c_time())
            n_time = x
    return n_time

def time_convert(x):
    hour = int(x[0:2])
    minute = int(x[3:5])
    second = int(x[6:8])
    time = (hour * 24 + minute) * 60 + second
    return time

def c_time():
    time = datetime.now()
    hour = int(time.strftime("%H"))
    minute = int(time.strftime("%M"))
    second = int(time.strftime("%S"))
    time2 = (hour * 24 + minute) * 60 + second
    return time2

n = input().split(" ")
print(n)
print(nearest_time(n))