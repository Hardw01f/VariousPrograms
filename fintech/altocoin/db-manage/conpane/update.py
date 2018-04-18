# -*- coding: utf-8 -*-

import requests
import MySQLdb
import re
import datetime

#mysqlに接続
conn = MySQLdb.connect(
        user='USERNAME',
        passwd='PASSWORD',
        host='HOSTNAME',
        db='DBNAME'
    )
#c = conn.cursor()


#binanceから価格情報を取得するメソッド
def bi_get():
    r = requests.get('https://api.binance.com/api/v3/ticker/price')
    res = r.json()
    return res


#coincheckから価格情報を習得するメソッド
def cc_get():
    r = requests.get('https://coincheck.com/api/ticker')
    res = r.json()
    return res


#binanceの板情報をトリミングするメソッド
def get_btcjpyrate():
    cc_str = str(cc_get())
    temp = cc_str.split(",")
    temp = temp[0].split(":")
    temp = temp[1]
    temp = temp.strip()
    now_btcjpyrate = temp
    return now_btcjpyrate

#binanceの板情報からレートの銘柄を判別するメソッド
def jadge_brandname(brand):
    brand = str(brand)
    if brand.find('BTC') > 0:
        flag = 'btc'
        #return flag
    elif brand.find('ETH') > 0:
        flag = 'eth'
        #return flag
    elif brand.find('BNB') > 0:
        flag = 'bnb'
        #return flag
    else:
        flag = "erroe"
        #return flag
    return flag


#coincheckから現在のBTCレートを抽出するメソッド
def trim_data(data):
    data = str(data)
    data = data.replace("}","")
    data = data.replace("'","")
    return data


#現在のBTCレートとbinanceのレートから日本円レートを計算するメソッド
def calcurate_jpy(coinrate,btcjpyrate):
    coinrate = float(coinrate)
    btcjpyrate = float(btcjpyrate)
    jpyrate = coinrate * btcjpyrate
    return jpyrate

#現在の時刻を取得するメソッド
def get_time():
    now = datetime.datetime.now()
    return now


if __name__ == "__main__":
    c = conn.cursor()
    #print(bi_get())
    #print(cc_get())
    btcjpyrate = get_btcjpyrate()
    print(btcjpyrate)
    #print(bi_get())
    all_data = bi_get()
    for n in all_data:
        #print(n)
        #print(type(n))
        num = str(n)
        num = num.split(" ")
        brand = num[1].replace(",","")
        brand = brand.split("'")
        brand = brand[1]
        btcrate = trim_data(num[3])
        #print(num)
        #print("brand:",brand)
        #print(jadge_brandname(brand))
        #print(btcrate)
        if jadge_brandname(brand) == 'btc':
            jpy = calcurate_jpy(btcrate,btcjpyrate)
            time = get_time()
            sql = 'update btc set btcrate=%s,jpyrate=%s,time=%s where brand=%s'
            c.execute(sql,(btcrate,jpy,time,brand))
            #print(brand)
            #print(btcrate)
            #print(jpy)
        elif jadge_brandname(brand) == 'eth':
            sql = 'update eth set ethrate=%s,time=%s where brand=%s'
            c.execute(sql,(btcrate,time,brand))
            #print(brand)
            #print(btcrate)
        elif jadge_brandname(brand) == 'bnb':
            sql = 'update bnb set bnbrate=%s,time=%s where brand=%s'
            c.execute(sql,(btcrate,time,brand))
            #print(brand)
            #print(btcrate)
        else:
            pass
            #print(brand)
            #print(btcrate)
        conn.commit()

        #c.close()
        #conn.close()
