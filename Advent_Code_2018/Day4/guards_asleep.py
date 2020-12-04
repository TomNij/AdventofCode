import numpy as np
import re
from collections import defaultdict
from datetime import datetime

g = open("C:/Users/tom/Documents/PythonCourse/Advent_Code_2018/Day4/input.txt", "r")
logs =  g.readlines()
logs = [log.strip() for log in logs]
g.close()
#sort logs using lambda:

get_date = lambda str: datetime.strptime(re.search('\[(.*)\]', str).group(1),'%Y-%m-%d %H:%M') #return datetime obj based on strings
logs.sort(key=get_date)

#parse date, time, id, message from log entries:
#per entry update the sleep array with zeroes if he wakes up and 1's if asleep
def sleep_parser(log):
    expr = '\[(.*)\]\s(.*\s.*)'
    date_time_obj = datetime.strptime(re.search(expr, log).group(1),'%Y-%m-%d %H:%M')
    date = str(datetime.date(date_time_obj))
    time = datetime.time(date_time_obj)
    mssg = re.search(expr, log).group(2)
    return date,time,mssg

sleep_dict = defaultdict()
sleep_arr = np.zeros((60))
id = '0'
for log in logs:
    date, time, mssg = sleep_parser(log)
    minute = time.minute
    try: #runs for a new guard line, save old sleep_arr to right guard
        old_id = id
        id = re.search('Guard #(\d+)', mssg).group(1)
        print(f"{date}, Guard id = {old_id},slept {sum(sleep_arr)} min.")
        if old_id in sleep_dict.keys():
            sleep_dict[old_id] = np.vstack((sleep_dict[old_id], sleep_arr))  # goes wrong
        else:  # first time a new guard is logged
            sleep_dict[old_id] = sleep_arr

        sleep_arr = np.zeros((60))
    except(AttributeError):
       if mssg == 'falls asleep':
           sleep_arr[minute:] = 1 #asleep = 1
       else:#wakes up
           sleep_arr[minute:] = 0

sleep_dict.pop('0', None)
max_sleep = 0
max_sleep_id = ''
freq_sleep_min = 0
freq_sleep_id = ''
for guard_id in sleep_dict.keys():
    tot_sleep = sum(sum(sleep_dict[guard_id]))
    print(f"{guard_id}, total minutes asleep: {tot_sleep}")
    max_sleep_min = int(np.argmax(np.sum(sleep_dict[guard_id], 0)))
    max_sleep_val = np.max(np.sum(sleep_dict[guard_id], 0))
    print(f"{guard_id}, was asleep: {max_sleep_val} times on minute: {max_sleep_min}")
    if tot_sleep > max_sleep:
        max_sleep = tot_sleep
        max_sleep_id = guard_id
    if max_sleep_val > freq_sleep_min:
        freq_sleep_min = max_sleep_min
        freq_sleep_id = guard_id
guard = int(max_sleep_id)
max_sleep_min = int(np.argmax(np.sum(sleep_dict[max_sleep_id],0))) #add over rows
print(guard)
print(max_sleep_min)
print(f"Answer 1: {guard*max_sleep_min}")

print(f"Answer 2: {freq_sleep_id}*{freq_sleep_min} = {int(freq_sleep_id)*int(freq_sleep_min)}")