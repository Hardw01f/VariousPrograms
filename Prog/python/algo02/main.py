# coerce -*- UTF-8

import tool
import sys

array1=[8,1,-1,2]
array2=[1,2,-3,-1]
array3=[0,-1,-1,-1]

def pibot_calcurate(array1,array2,array3):
    pibot_z=tool.minisave(array3)
#pibot_z=(最小値、最小値のリスト番号)を獲得

    print("Zの最小値は" +str(pibot_z[0])+ "で、最小値の位置は " + str(pibot_z[1]) + "番目。" )

###ピボット決定のプロセス

#各列の要素が負の値であるときの処理
    if (array1[pibot_z[1]]<=0) and (array2[pibot_z[1]]<=0):
        print("どちらも負の値であるので選択不可")
        temparray=array3
        save_val=pibot_z[0] #ピボットの値の保存
        #print("save_val= :" + str(save_val))
        save_num=pibot_z[1] #ピポットの番号の保存
        #print("save_num= :" + str(save_num))
        temparray[pibot_z[1]]=0 #
        #print("temparray= " + str(temparray))
        pibot_z=tool.minisave(temparray) 
        #print("pibot_z= " + str(pibot_z))
        array3[save_num]=save_val  #取り外した値の戻し
        #print(array3)
        #sys.exit()
        #array3.insert(save_val,save_num)
        #print("chack array3" + str(array3))
        print("1:Zの最小値は" +str(pibot_z[0])+ "で、最小値の位置は " + str(pibot_z[1]) + "番目。" )
        if (array1[pibot_z[1]]<=0) and (array2[pibot_z[1]]<=0):
            print("どちらも負の数であるので選択不可")
            print("chack array3 : " + str(temparray))
            temparray.pop(pibot_z[1])
            print(temparray)
            pibot_z=tool.minisave(temparray)
            print("chack array3 " + str(array3))
            print("2:Zの最小値は" +str(pibot_z[0])+ "で、最小値の位置は " + str(pibot_z[1]) + "番目。" )
            if (array1[pibot_z[1]]<=0) and (array2[pibot_z[1]]<=0):
                print("最適解なし")
                sys.exit()


#ピボットの決定
    num=tool.judge(array1[0],array1[pibot_z[1]],array2[0],array2[pibot_z[1]])
#定数/各ピボット列の行の値から判断するピボット行の決定
    print("定数/ピボット列の数値=" + str(num[0]) + ",ピボットの行番号: " + str(num[1]))
#temppib: 仮のリスト保存用
    temppib="array"+str(num[1])

    if temppib == 'array1':
        pib_array=array1   #pib_array : リスト確定用の保存
    else:
        pib_array=array2

#ピボット行の決定
    pibotarray=pib_array
    print("ピボットのある列は " + str(pibotarray))

#ピボット決定
    pibot=pib_array[pibot_z[1]]
    print("ピボットは " + str(pibot)+" になる")


##各行の計算

    for num in range(0,4):
        #print(num)
        pibotarray[num]=pibotarray[num]/pibot
    #print(pibotarray)

    mother1=array1[pibot_z[1]] #各行のピボット列の値
    mother2=array2[pibot_z[1]]
    mother3=array3[pibot_z[1]]

    if temppib == 'array1':
        for num in range(0,4):
            array2[num]=array2[num]-(pibotarray[num]*mother2)
            array3[num]=array3[num]-(pibotarray[num]*mother3)
        #print(array2)
        #print(array3)
        array1=pibotarray
        #print(array1)
    elif temppib == 'array2':
        #print("select array2")
        for num in range(0,4):
            #print("----------")
            #print(num)
            #print(pibot_z[1])
            #print("1:chack array1[pibot] = " + str(array1[pibot_z[1]]))
            #print("chack calcrate : " + str(array1[num]) +"-"+str(pibotarray[num])+"*"+str(mother1))
            array1[num]=array1[num]-(pibotarray[num]*mother1)
            #print("array1 :" + str(num) + "  " + str(array1[num]))
            #print("chack array3 = " + str(array3[num]))
            array3[num]=array3[num]-(pibotarray[num]*mother3)
            #print("2:chack array1[pibot] = " + str(array1[pibot_z[1]]))
            #print("chack " + str(array3))
        #print(array1)
        #print(array3)
        array2=pibotarray
        #print(array2)
    else:
        print("error")
        sys.exit()

    print("-------------------------")
    print(array1)
    print(array2)
    print(array3)
    print("-------------------------")

    if array3[0]>=0 and array3[1]>=0 and array3[2]>=0 and array3[3]>=0:
        print("暫定最適解である")

    return array1,array2,array3



JUDGE=1

while JUDGE==1:
    list=pibot_calcurate(array1,array2,array3)
    array1=list[0]
    array2=list[1]
    array3=list[2]

    if array3[0]>=0 and array3[1]>=0 and array3[2]>=0 and array3[3]>=0:
            print("暫定最適解である")
            sys.exit()
    


'''
list=pibot_calcurate(array1,array2,array3)
print(list)
array1=list[0]
array2=list[1]
array3=list[2]

print(array1)
print(array2)
print(array3)

if array3[0]>=0 and array3[1]>=0 and array3[2]>=0 and array3[3]>=0:
        print("暫定最適解である")
        sys.exit()
else: 
    list=pibot_calcurate(array1,array2,array3)
    print(list)
    array1=list[0]
    array2=list[1]
    array3=list[2]

    print(array1)
    print(array2)
    print(array3)

'''
