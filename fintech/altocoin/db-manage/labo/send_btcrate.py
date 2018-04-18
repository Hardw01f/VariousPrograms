# -*- coding: utf-8 -*-

import requests
import MySQLdb

conn = MySQLdb.connect(
        user='USERNAME',
        passwd='PASSWORD',
        host='HOSTNAME',
        db='DBNAME'
    )


def cc_get():
    r = requests.get('https://coincheck.com/api/ticker')
    res = r.json()
    return res


def trim_data(data):
    data = str(data)
    data = data.split(" ")
    data = data[3].replace(",","")
    return data

def feuch():
    sql='select * from btc'
    res = c.fetchone(sql)
    return res


if __name__ == "__main__":
    c = conn.cursor()
    res = trim_data(cc_get())
    rate = float(res)
    print(res)
    sql = 'select * from btc'
    c.execute(sql)
    while True:
        res = c.fetchone()
        print(res)
        if res == None:
            break
        #print(res[0],res[1])
        brand = str(res[0])
        brand = brand.replace("'","")
        brandrate = float(res[1])
        print('brand',brand)
        print('brandrate',str(brandrate))
        jpy = rate * brandrate
        print('jpyrate',jpy)
        up_sql=('update btc set jpyrate= %s where brand= %s')
        #print(up_sql)
        c.execute(up_sql,(jpy,brand))
    #conn.commit()
