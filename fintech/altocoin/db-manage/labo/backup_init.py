# -*- coding: utf-8 -*-

import requests
import MySQLdb
import re


conn = MySQLdb.connect(
        user='USERNAME',
        passwd='PASSWORD',
        host='HOSTNAME',
        db='DBNAME'
    )
#c = conn.cursor()


def bi_get():
    r = requests.get('https://api.binance.com/api/v3/ticker/price')
    res = r.json()
    return res
    
def cc_get():
    r = requests.get('https://coincheck.com/api/ticker')
    res = r.json()
    return res

def get_btcjpyrate():
    cc_str = str(cc_get())
    temp = cc_str.split(",")
    temp = temp[0].split(":")
    temp = temp[1]
    temp = temp.strip()
    now_btcjpyrate = temp
    return now_btcjpyrate

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

def trim_data(data):
    data = str(data)
    data = data.replace("}","")
    data = data.replace("'","")
    return data

def calcurate_jpy(coinrate,btcjpyrate):
    coinrate = float(coinrate)
    btcjpyrate = float(btcjpyrate)
    jpyrate = coinrate * btcjpyrate
    return jpyrate

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
        print(num)
        print("brand:",brand)
        #print(jadge_brandname(brand))
        #print(btcrate)
        if jadge_brandname(brand) == 'btc':
            jpy = calcurate_jpy(btcrate,btcjpyrate)
            sql = 'insert into btc(brand,btcrate,jpyrate) values (%s,%s,%s)'
            c.execute(sql,(brand,btcrate,jpy))
            print(brand)
            print(btcrate)
            print(jpy)
        elif jadge_brandname(brand) == 'eth':
            sql = 'insert into eth(brand,ethrate) values (%s,%s)'
            c.execute(sql,(brand,btcrate))
            print(brand)
            print(btcrate)
        elif jadge_brandname(brand) == 'bnb':
            sql = 'insert into bnb(brand,bnbrate) values (%s,%s)'
            c.execute(sql,(brand,btcrate))
            print(brand)
            print(btcrate)
        else:
            print(brand)
            print(btcrate)
        conn.commit()

        #c.close()
        #conn.close()
