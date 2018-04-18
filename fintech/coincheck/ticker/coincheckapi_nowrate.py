import subprocess
import sys

PRICE = 3000
FLAG = 0


#それぞれの文字列をfloat化してdiffを計算するメソッド
def calcurate(now_rate,later_rate):
    now = float(now_rate)
    later = float(later_rate)
    result = now - later
    print(result)
    return result

#diffによる条件分岐メソッド
def select(result):
    if result < 0 and result < -PRICE :
        print("大幅下落時の処理")
        #FLAG = 0
        return 0
    elif result > 0 and result > PRICE :
        print("大幅高騰時の処理")
        #FLAG = 1
        return 1 
    elif result == 0:
        print("変化なし")
    else:
        print("大幅な変化なし")

#slackにpost_apiを叩くメソッド
def send_slack(FLAG,now_rate,result):
    if FLAG == 1:
        cmd = "curl -XPOST -d token=取得したtoken -d channel=#btc_channel -d text=高騰中:Now_changing_rate_:__now_rate:" + str(now_rate) + "__:value_change:" + str(result) + " -d username=btc_alert https://slack.com/api/chat.postMessage"
        subprocess.call( cmd.split(" ") )
    elif FLAG == 0:
        cmd = "curl -XPOST -d token=取得したtoken -d channel=#btc_channel -d text=暴落中:Now_changing_rate_:__now_rate:" + str(now_rate) + "__:value_change:" + str(result) + " -d username=btc_alert https://slack.com/api/chat.postMessage"
        subprocess.call( cmd.split(" ") )
    else:
        print("Nothing alert")


#curlでcoincheckからパラメータ取得
cmd = "curl GET https://coincheck.com/api/ticker"
now_price = subprocess.check_output( cmd.split(" ") )

#前回スクリプト実行時のパラメータを取得
for later_rate in open('/home/shambara/api/file.txt', 'r'):
    print(later_rate)


#現在のパラメータのトリミング
print(now_price)
now_price = str(now_price)
now_price = now_price.split(",")

numresult = now_price[0].split(":")
now_rate = numresult[1]

#diff計算
result = calcurate(now_rate,later_rate)
print("result is " +str(result))

#diffにより処理分岐
FLAG = select(result)

print("FLAG is " + str(FLAG))

#slackにapiを叩く
send_slack(FLAG,now_rate,result)


#現在のパラメータを外部ファイルに保存
now_rate = str(now_rate)
file = open('/home/shambara/api/file.txt','w')
file.write(now_rate)
file.close()

