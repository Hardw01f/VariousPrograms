#coding:utf-8

import sqlite3
import sys
import os
#sys.path.append(os.path.dirname(__file__)+'/nfcpy')
#sys.path.append('/usr/local/lib/python2.7/site-packages')
import nfc
import time
from kafka import KafkaConsumer, KafkaProducer
from datetime import datetime as dt

def sendidm(idm):
	while True:
		producer = KafkaProducer(bootstrap_servers='IPADDR:9092')
		#producer.send('test',b"idm")
                tdatetime = dt.now()
                tstr = tdatetime.strftime('%Y/%m/%d %H:%M:%S')
                info = ('%s,321,0,' % idm)
                merge = info+tstr
		producer.send('TOPICNAME',str(merge))
		#producer.send('test',"%s" % idm)
		print(merge)
		return
		
def leave(tag):
	#print tag
	line = str(tag)
    	line = line.split()
    	idm = line[4][3:19]
    	print idm
	print("leave") 
    	sendidm(idm)



#clf_IN = nfc.ContactlessFrontend('usb:001:IN_PASORI')
clf_OUT = nfc.ContactlessFrontend('usb:001:027')

while clf_OUT.connect(rdwr = {'on-connect':leave}):
	print 'Please tache your ID-card '
	#clf_OUT.connect(rdwr = {'on-connect':leave})
sys.exit(1)

