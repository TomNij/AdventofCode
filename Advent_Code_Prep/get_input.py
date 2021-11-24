import datetime
import requests
import os
import browser_cookie3
import sys

now = datetime.datetime.now()
yr = str(now.year)
day_today = str(now.day)

# Get cookies from the browser
cj = browser_cookie3.chrome()
if not (".adventofcode.com" in str(cj)):
    cj = browser_cookie3.chrome()

# If we provide an argument, use it as the desired day. Ex: ./startDay.py 5. Otherwise use day_today
if len(sys.argv) > 1:
    day = int(sys.argv[1])
    if day < 0 or day > 31 or day > int(day_today):
        exit("Day is not valid")
else:
    day = day_today

print(f"Initializing day {day}")
path = f'../Advent_Code_{yr}/Input_files/{day_today}.txt'
if not os.path.exists(path):
    r = requests.get(f"https://adventofcode.com/{yr}/day/{day}/input", cookies=cj)
    with open(path, "w") as f:
        f.write(r.text)