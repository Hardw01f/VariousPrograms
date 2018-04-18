from kafka import KafkaConsumer, KafkaProducer

def main():
	consumer = KafkaConsumer(bootstrap_servers='10.0.2.4:9092',auto_offset_reset='earliest')
	consumer.subscribe(['test30'])

	for message in consumer:
		print message

if __name__ == "__main__":
    main()
