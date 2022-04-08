#!/usr/bin/env python
import time
import sys
from subprocess import Popen

NYC_DATA = '/mnt/ess_storage/DN_1/storage/home/akorneev/temp_tables/nyc_filtering/df_'
save_path = '/mnt/ess_storage/DN_1/storage/home/akorneev/temp_tables/nyc_filtering/y_pred'

total_number = 5089584
proc_num = 30
shift = int(total_number/proc_num)
print('shift = ', shift)

i = 25
start = i * shift
finish = 0
while( finish != total_number):
    finish = start + shift
    if finish > total_number:
        finish = total_number
    #cmd = f"/home/jovyan/notebooks/Aleksei/clean_data.py {start} {finish} {NYC_DATA} {save_path}"
    cmd = [ sys.executable, '/home/jovyan/notebooks/Aleksei/clean_data.py', str(start), str(finish), NYC_DATA, save_path,]
    print(f"cmd {i}", Popen(cmd).pid)
    start = finish
    i += 1

print('Clean_ny is finished')