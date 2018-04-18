import requests
import socket
    
def cc_get():
    r = requests.get('https://coincheck.com/api/ticker')
    res = r.json()
    return res

def trim(param):
    res = str(param)
    res = res.split(" ")
    res = res[1].replace(",","")
    return res

def calcu_rate(param,jpy):
    percoin = int(jpy)/float(param)
    return percoin

def calcu_coin(param,val):
    coinval = float(param)*float(val)
    return coinval

if __name__ == "__main__":
    port = 9999
    bufsize = 4096

    ssock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ssock.bind(('0.0.0.0',port))
    ssock.listen(1)

    csock, caddr = ssock.accept()
    req = ''
    while True:
        req = req + csock.recv(bufsize)
        if req.find('\r\n\r\n') >= 0:
            break
    csock.send('Hellw,world!')
    csock.close()

    ssock.close()

    get = cc_get()
    now_rate = trim(get)
    #print(now_rate)

    print('')
    res = calcu_rate(now_rate,10000)
    print("10000JPY = "+str(res)+" BTCcoin")
    res = calcu_rate(now_rate,1000)
    print('1000JPY = '+str(res)+' BTCcoin')
    res = calcu_rate(now_rate,100)
    print('100JPY = '+str(res)+' BTCcoin')

    print("-------------------------------------")

    res = calcu_coin(now_rate,0.1)
    print('0.1 BTCcoin = '+ str(res) + ' JPY') 
    res = calcu_coin(now_rate,0.01)
    print('0.01 BTCcoin = '+ str(res) + ' JPY') 
    res = calcu_coin(now_rate,0.001)
    print('0.001 BTCcoin = '+ str(res) + ' JPY')

    print('-------------------------------------')

    res = calcu_coin(now_rate,0.5)
    print('0.5 BTCcoin = '+ str(res) + ' JPY') 
    res = calcu_coin(now_rate,0.05)
    print('0.05 BTCcoin = '+ str(res) + ' JPY') 
    res = calcu_coin(now_rate,0.005)
    print('0.005 BTCcoin = '+ str(res) + ' JPY')

    print('--------------------------------------')
