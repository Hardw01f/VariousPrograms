# cording:utf-8
import calc


num=input("初期解の数を入力してください　")

list=[]                               #初期集団用のリスト
sum=[]                                #暫定解の検出時のリスト保存用
sum_arrey=[]



for x in range(int(num)):
    print("続けて、４つの要素を\"１つずつ\"入力してください")
    for i in range(4):
        m=int(input())
        list.append(m)
        print(list)
    log=calc.caluculate(list)         #計算関数
    ans=log.split(" ")
    print("最適解は"+str(ans[0]))
    print(str(list)+"の最適解の組み合わせは"+str(ans[1])+str(ans[2])+str(ans[3])+str(ans[4]))
    list.clear()                      #リストの開放
    print((str(ans[1])+str(ans[2])+str(ans[3])+str(ans[4])))    
    z=int(log[0:2])
    z_arrey=str(log[3:13])
    sum.append(z)
    sum_arrey.append(z_arrey)
    #print(sum)
    #print(sum_arrey)
    sum=sorted(sum)
    #print(sum)
    print("この集団の最適解は"+str(sum[0]))
