# coding: UTF-8

# 引数として渡したリストの中から最小値の値と最小値のリスト番号を返す関数
# minmum  最小値の保存用変数
# pibotnumbert 最小値のリスト番号保存用変数


def minisave(array):
    ansnum=0
    for num in range(len(array)):
        #print("len(array)= "+str(num))
        #print(num)
        #print(array)
        #print(len(array))
        #print(array[num])
        #print(array[num+1])
        if array[num] <0:
            if ansnum <= abs(array[num]):
                ansnum=array[num]
                pibotnumber=num
            else:
                ansnum=ansnum
            #pibotnumber=num

    return ansnum,pibotnumber



#テスト用構文
'''
list=[0,-1,-10,-6]

res=minisave(list)

print(res)
'''

#num1/mo1,num2/mo2の除算をして値が小さい方の分母を返す

def judge(num1,mo1,num2,mo2):
    if mo1<=0:
        if mo2<=0:
            print("error")
    if mo2<=0:
        jud1=num1/mo1
        return jud1,1
    jud1=num1/mo1
    jud2=num2/mo2
    if jud1<jud2:
        return jud1,1
    return jud2,2


#テスト構文

'''
num1=8
mo1=2
num2=1
mo2=-1

res=judge(num1,mo1,num2,mo2)
print(res)
'''

