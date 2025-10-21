from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def send_message(topic, message):
    try:
        future = producer.send(topic, message)
        record_metadata = future.get(timeout=10)
        print(f"Message sent to {record_metadata.topic} partition {record_metadata.partition} offset {record_metadata.offset}")
    except Exception as e:
        print(f"Error sending message: {e}")

if __name__ == "__main__":
    for i in range(10):
        message = {
            'id': i,
            'timestamp': time.time(),
            'data': f'Message {i}'
        }
        send_message('students', message)
    producer.close()