# coding: utf-8
import tool
import copy

a=[6,1,9,3]
b=[2,5,7,8]
c=[6,3,5,4]
d=[3,5,2,1]


def caluculate(line):
    
    #line=[3,4,1,2]            #初期集団
    temp=0                    #データ入替時の仮の変数
    arrey=copy.deepcopy(line) #lineをコピーして実際に使うリストの用意
    time=0                    #ある初期集団の解
    tempval=0                 #ある初期集団の暫定解
    temparrey=0               #暫定解が更新された時の要素

    for i in range(1,7): #　6回の組み合わせなので6ループ
        if i==1:         #　1回目の摂動
            temp=arrey[0]                          #値の入替
            arrey[0]=arrey[1]
            arrey[1]=temp
            print(arrey)
            time=a[arrey[0]-1]+b[arrey[1]-1]+c[arrey[2]-1]+d[arrey[3]-1] 
            #入替後のそれぞれのリストの値に対する時間計算
            print(time)
            tempval=time                           #初期ループなので出た最適解を暫定解に設定
            temparrey=copy.deepcopy(arrey)         #初期ループなので出た最適解の組み合わせを保存
            print("暫定解は"+str(tempval))
        elif i==2:       #　2回目の摂動
            print("------------")
            temp=arrey[1]
            arrey[1]=arrey[2]
            arrey[2]=temp
            print(arrey) 
            time=a[arrey[0]-1]+b[arrey[1]-1]+c[arrey[2]-1]+d[arrey[3]-1]
            print(time)
            tempval=tool.compere(tempval,time)                     #最適解と暫定解の比較計算
            temparrey=tool.comparrey(tempval,time,arrey,temparrey) #最適化の組み合わせの評価関数
            print("暫定解は"+str(tempval))
        elif i==3:       #　3回目の摂動
            print("------------")
            temp=arrey[2]
            arrey[2]=arrey[3]
            arrey[3]=temp
            print(arrey) 
            time=a[arrey[0]-1]+b[arrey[1]-1]+c[arrey[2]-1]+d[arrey[3]-1]
            print(time)
            tempval=tool.compere(tempval,time)
            temparrey=tool.comparrey(tempval,time,arrey,temparrey)
            print("暫定解は"+str(tempval))
        elif i==4:       #　4回目の摂動
            print("------------")
            temp=arrey[0]
            arrey[0]=arrey[3]
            arrey[3]=temp
            print(arrey) 
            time=a[arrey[0]-1]+b[arrey[1]-1]+c[arrey[2]-1]+d[arrey[3]-1]
            print(time)
            tempval=tool.compere(tempval,time)
            temparrey=tool.comparrey(tempval,time,arrey,temparrey)
            print("暫定解は"+str(tempval))
        elif i==5:       #　5回目の摂動
            print("------------")
            temp=arrey[0]
            arrey[0]=arrey[2]
            arrey[2]=temp
            print(arrey) 
            time=a[arrey[0]-1]+b[arrey[1]-1]+c[arrey[2]-1]+d[arrey[3]-1]
            print(time) 
            tempval=tool.compere(tempval,time)
            temparrey=tool.comparrey(tempval,time,arrey,temparrey)
            print("暫定解は"+str(tempval))
        elif i==6:       #　6回目の摂動
            print("------------")
            temp=arrey[1]
            arrey[1]=arrey[3]
            arrey[3]=temp
            print(arrey) 
            time=a[arrey[0]-1]+b[arrey[1]-1]+c[arrey[2]-1]+d[arrey[3]-1]
            print(time)
            tempval=tool.compere(tempval,time)
            temparrey=tool.comparrey(tempval,time,arrey,temparrey)
            print("暫定解は"+str(tempval))
        else:
            break

        arrey=copy.deepcopy(line)      #リストの初期化
        time=0                         #最適解を初期化
        temp=0                         #仮の箱の初期化 
    
    return str(tempval)+" "+str(temparrey)
