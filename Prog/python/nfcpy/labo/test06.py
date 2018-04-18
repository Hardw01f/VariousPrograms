# coding: utf-8

# -----------------------------
# name : RYO Tsukayama
# aim : Pasori IC-card authenticate-system
# date : 2017/08/11
# -----------------------------








import sys
import os
sys.path.append(os.path.dirname(__file__) + '/nfcpy')
import nfc
import subprocess
import os
import os.path
import shutil

#ユーザーの数
USERCOUNT = 4

datalist = [["****************","USERNAME00"],
            ["****************","USERNAME01"],
            ["****************","USERNAME02"],
            ["****************","USERNAME03"],
            ]

#タッチされたときに実行する関数
def judge(tag):
    print tag
    line = str(tag)
    line = line.split()
    idm = line[4][3:19]
    #print idm
    #以下でdatalistからIDmとユーザーの照合をかける
    i = 0
    args_on = ['sudo','ifconfig','eth0','up'] 
    args_off = ['sudo','ifconfig','eth0','down']

    while i <= USERCOUNT:
        if idm == datalist[i][0]:
            print "-------------------------------------------------------------------------"
            print " "
            print "ID=" + idm + ", YOU ARE " + datalist[i][1] + " , YOU ARE AUTHENTICATED!!!"
            #認証後のIDmディレクトリの存在確認
            if os.path.exists(idm):
                #IDmディレクトリが存在していた場合
                print("インターフェースダウン")
                shutil.rmtree(idm)
                #break
                try:
                    res = subprocess.check_output(args_off)
                except:
                    print "Error." + res
                    print res
                    break
		break
            else:
                #IDmディレクトリが存在していなかった場合
                print("インターフェース起動")
                os.mkdir(idm)
                try:
                    res = subprocess.check_output(args_on)
                except:
                    print "Error." + res
                    print res
                    break
		break
        else:
            i = i + 1
            if i == USERCOUNT:  #カウント数がUSERCOUNT,datalistの要素数を超えた時の処理
                print "---------------------------------"
                print " "
                print "YOU ARE UNKNOWN , SO GET OUT!!!!"
                break
    

#USBカードリーダーと接続
clf = nfc.ContactlessFrontend('usb')

#恐らく、タッチされた時に呼び出す関数の設定
rdwr = {'on-connect':judge}

print 'Please tache your ID-card '
#clf.connectでPaSoRiを起動
clf.connect(rdwr=rdwr)
#print 'finish'
