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


def setup():
	producer = KafkaProducer(bootstrap_servers='IPADDR:9092')
	return producer

def sendidm(idm,producer):
	while True:
		idm = str(idm)
		#producer = KafkaProducer(bootstrap_servers='10.0.2.4:9092')
		#producer.send('test05','334')
		tdatetime = dt.now()
		tstr = tdatetime.strftime('%Y:%m:%d:%H:%M:%S')
		info = ('%s,321,1,' % idm)
		print(info)
		merge = info+str(tstr)
		print merge
		merge = str(merge)
		producer.send('test06',b'%s' % (merge))
		#producer.send('test05',b"%s" % idm)
		print(merge)
		producer.flush()
		producer.close()
		return

'''
if __name__ == "__main__":
	producer = setup()
	sendidm('012E4573E14A358D',producer)
'''

def attend(tag):
	#print tag
	producer = setup()
	line = str(tag)
    	line = line.split()
    	idm = line[4][3:19]
    	print idm
	print("attend")
    	sendidm(idm,producer)

clf_IN = nfc.ContactlessFrontend('usb:001:IN_PASORI')
#clf_OUT = nfc.ContactlessFrontend('usb:001:OUT_PASORI')

while clf_IN.connect(rdwr = {'on-connect':attend}):
	print 'Please tache your ID-card '
	#clf_IN.connect(rdwr = {'on-connect':attend})
sys.exit(1)

#clf_OUT.connect(rdwr = {'on-connect':leave})
