import time
import subprocess

cmd = 'python3.6 update.py'
while 1:
    try:
        res = subprocess.run(cmd.split(" "))
    except:
        res = 'error'
    #print(res)
    time.sleep(15)
