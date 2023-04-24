from kafka import KafkaConsumer
consumer = KafkaConsumer('dbserver1.inventory.customers',
                         bootstrap_servers=['localhost:9092'],
                         group_id='my')
for message in consumer:
    print (message)