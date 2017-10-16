import sys
import subprocess

def get_parameter():
    cmd = "curl GET https://coincheck.com/api/ticker"
    parameter = subprocess.check_output( cmd.split(" "))
    #print(parameter)
    return parameter

def send_slack(parameter):
    parameter = str(parameter)
    cmd = "curl -XPOST -d token=取得したトークン -d channel=#btc_channel -d text=now_BTC_rate_:" + parameter + " -d username=BTC_Regular https://slack.com/api/chat.postMessage"
    subprocess.call(cmd.split(" "))






if __name__ == "__main__":
    get_parameter()


