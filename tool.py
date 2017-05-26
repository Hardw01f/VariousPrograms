import copy

def compere(tempval,time):
#２つの最適解を比べて最小な方をとる関数
#compere(現在の暫定解,計算の結果の最適解)
    if tempval > time:
        tempval=time
        return tempval
    else:
        return tempval

def comparrey(tempval,time,arrey,temparrey):
#暫定解のリストの比較と保存をする関数
#comparrey(現在の暫定解,計算の結果の最適解,現在の結果のリスト,現在の暫定解のリスト)
    if tempval==time:
        temparrey=arrey
        return temparrey
    else:
        return temparrey


