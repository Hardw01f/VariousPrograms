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
		info = ('%s,321,1,' % idm)
		merge = info+tstr
		#print merge
		producer.send('TOPICNAME',str(merge))
		#producer.send('test',"%s" % idm)
		print(merge)
		return
		
def attend(tag):
	#print tag
	line = str(tag)
    	line = line.split()
    	idm = line[4][3:19]
    	print idm
	print("attend")
    	sendidm(idm)

clf_IN = nfc.ContactlessFrontend('usb:001:025')
#clf_OUT = nfc.ContactlessFrontend('usb:001:OUT_PASORI')

while clf_IN.connect(rdwr = {'on-connect':attend}):
	print 'Please tache your ID-card '
	#clf_IN.connect(rdwr = {'on-connect':attend})
sys.exit(1)

#clf_OUT.connect(rdwr = {'on-connect':leave})
