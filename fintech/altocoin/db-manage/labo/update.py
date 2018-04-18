# -*- coding: utf-8 -*-

import requests
import MySQLdb


conn = MySQLdb.connect(
        user='USERNAME',
        passwd='PASSWROD',
        host='HOSTNAME',
        db='DBNAME'
    )


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
    elif brand.find('USDT') > 0:
        flag = 'usdt'
        return flag
    else:
        flag = "erroe"
        #return flag
    return flag

def trim_bi_data(data):
    data = str(data)
    data = data.replace("}","")
    data = data.replace("'","")
    return data

def trim_cc_data(data):
    data = str(data)
    data = data.split(" ")
    data = data[1].replace(",","")
    return data

def calcurate_jpy(btcrate,btcjpyrate):
    btcrate = float(btcrate)
    btcjpyrate = float(btcjpyrate)
    jpyrate = btcrate * btcjpyrate
    return jpyrate


if __name__ == "__main__":
#print()はデバッグ用
    c = conn.cursor()
    get_btcjpyrate()
    #print(bi_get())
    res_cc_get = cc_get()
    btcjpyrate = trim_cc_data(res_cc_get)
    print(res_cc_get)
    print(btcjpyrate)
    all_data = bi_get()
    for n in all_data:
        #print(n)
        #print(type(n))
        num = str(n)
        num = num.split(" ")
        brand = num[1]
        btcrate = trim_bi_data(num[3])
        #print(num)
        #print(brand)
        #print(jadge_brandname(brand))
        #print(btcrate)
        if jadge_brandname(brand) == 'btc':
            jpyrate = calcurate_jpy(btcrate,btcjpyrate)
            #sql = 'update btc set btcrate = %s where brand = %s'
            sql = 'update btc set btcrate = %s,jpyrate = %s where brand = %s'
            c.execute(sql,(btcrate,jpyrate,brand))
            #c.execute(sql,(btcrate,brand))
            print(brand)
            print(btcrate)
            print('jpyrate:',jpyrate)
        elif jadge_brandname(brand) == 'eth':
            sql = 'update eth set btcrate = %s where brand = %s'
            c.execute(sql,(btcrate,brand))
            print(brand)
            print(btcrate)
        elif jadge_brandname(brand) == 'bnb':
            sql = 'update bnb set btcrate = %s where brand = %s'
            c.execute(sql,(btcrate,brand))
            print(brand)
            print(btcrate)
        else:
            pass
            print(brand)
            print(btcrate)
        conn.commit()
