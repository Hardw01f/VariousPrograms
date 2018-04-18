#!/bin/sh
~/kafka_2.11-0.11.0.1/bin/zookeeper-server-start.sh config/zookeeper.properties &
~/kafka_2.11-0.11.0.1/bin/kafka-server-start.sh config/server.properties &
