import subprocess
import os

def call():
    first_cmd='ps aux'
    second_cmd='grep main.py'
    f_res = subprocess.Popen(first_cmd.split(" "),stdout=subprocess.PIPE)
    s_res = subprocess.Popen(second_cmd.split(" "),stdin=f_res.stdout,shell=True)
    #print( "process id = %s" % s_res.pid )
    s_res.terminate()
    print(s_res)
    #pid = str(s_res.pid)
    #kill_cmd = 'kill -9 '+pid
    #subprocess.run(kill_cmd.split(" "))
    return s_res

def jadge(res):
    return 0

if __name__ == "__main__":
    res = call()
    print(res)
    #print(type(res))

