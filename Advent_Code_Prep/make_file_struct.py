from pathlib import Path
import datetime
now = datetime.datetime.now()
yr = str(now.year)
Path("../Advent_Code_" + yr).mkdir(parents=True, exist_ok=True)
Path("../Advent_Code_" + yr + '/Input_files').mkdir(parents=True, exist_ok=True)
for day_nr in range(1,26):
    Path("../Advent_Code_" + yr + '/Day' + str(day_nr)).mkdir(parents=True, exist_ok=True)