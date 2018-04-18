import time
from kafka import KafkaConsumer, KafkaProducer
from datetime import datetime as dt

def main(idm):
	producer = KafkaProducer(bootstrap_servers='IPADDR:9092')
	counter = 0
	while True:
		producer.send('TOPICNAME', b"test")
		#time.sleep(1)
		counter+=1

		if counter == 10:
			break
		



if __name__ == "__main__":
	main('334')
