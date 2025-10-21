from kafka import KafkaConsumer
import json
from constants import STUDENT_QUEUE, QUEUE_URL

# Create a consumer instance
consumer = KafkaConsumer(
    STUDENT_QUEUE,
    bootstrap_servers=[QUEUE_URL],
    auto_offset_reset='earliest',  # Start from the beginning if no offset exists
    enable_auto_commit=True,
    group_id='my-consumer-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# Consume messages
print("Waiting for messages...")
try:
    for message in consumer:
        print(f"Topic: {message.topic}")
        print(f"Partition: {message.partition}")
        print(f"Offset: {message.offset}")
        print(f"Key: {message.key}")
        print(f"Value: {message.value}")
        print("-" * 50)
except KeyboardInterrupt:
    print("\nConsumer stopped")
finally:
    consumer.close()