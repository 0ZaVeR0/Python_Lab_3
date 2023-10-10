from datetime import datetime

def nearest_time(times: str) -> str:
    time_diff = 9999999999
    for x in times:
        if min(abs(time_convert(x) - c_time()), abs(time_convert(x) - time_convert('24:00:00') - c_time())) < time_diff:
            time_diff = abs(time_convert(x) - c_time())
            n_time = x
    return n_time

def time_convert(x:str) -> int:
    hour = int(x[0:2])
    minute = int(x[3:5])
    second = int(x[6:8])
    time = (hour * 24 + minute) * 60 + second
    return time

def c_time() -> int:
    time = datetime.now()
    hour = int(time.strftime("%H"))
    minute = int(time.strftime("%M"))
    second = int(time.strftime("%S"))
    time2 = (hour * 24 + minute) * 60 + second
    return time2

def main():
    n = input().split(" ")
    print(nearest_time(n))

if __name__ == "__main__":
    main()