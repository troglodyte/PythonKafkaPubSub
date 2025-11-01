from kafka import KafkaConsumer
import json
from constants import STUDENT_QUEUE, QUEUE_URL
from multiprocessing import Pool, cpu_count
import signal
import sys


class KafkaMessageConsumer:
    def __init__(self, num_workers=None):
        self.consumer = None
        self.pool = None
        self.num_workers = num_workers or cpu_count()

    def initialize_consumer(self):
        self.consumer = KafkaConsumer(
            STUDENT_QUEUE,
            bootstrap_servers=[QUEUE_URL],
            auto_offset_reset='earliest',  
            enable_auto_commit=True,
            group_id='my-consumer-group',
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )
        # Initialize process pool
        self.pool = Pool(processes=self.num_workers)

    @staticmethod
    def process_message(message_data):
        """Static method to process message - must be picklable"""
        topic, partition, offset, key, value = message_data
        print(f"Topic: {topic}")
        print(f"Partition: {partition}")
        print(f"Offset: {offset}")
        print(f"Key: {key}")
        print(f"Value: {value}")
        print("-" * 50)
        # Add your processing logic here
        return f"Processed message at offset {offset}"

    def start_consuming(self):
        print(f"Starting consumer with {self.num_workers} workers...")
        try:
            for message in self.consumer:
                # Extract message data as tuple
                message_data = (
                    message.topic,
                    message.partition,
                    message.offset,
                    message.key,
                    message.value
                )
                # Submit to process pool (async)
                self.pool.apply_async(
                    self.process_message,
                    args=(message_data,),
                    error_callback=lambda e: print(f"Error: {e}")
                )
        except KeyboardInterrupt:
            print("\nConsumer stopped")
        finally:
            self.close()

    def close(self):
        if self.pool:
            self.pool.close()
            self.pool.join()
        if self.consumer:
            self.consumer.close()


if __name__ == "__main__":
    consumer = KafkaMessageConsumer(num_workers=4)
    consumer.initialize_consumer()
    consumer.start_consuming()
