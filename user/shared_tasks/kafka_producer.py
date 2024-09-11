# kafka_producer.py

from confluent_kafka import Producer
from django.conf import settings
import json

class KafkaProducer:
    def __init__(self):
        self.producer = Producer(
            {
                'bootstrap.servers': settings.KAFKA_BROKER_URL,
                # 'debug': 'all'
            }
        )
    def delivery_report(self, err, msg):
        if err is not None:
            print(f"Message delivery failed: {err}")
        else:
            print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

    def publish_message(self, topic, message):
        self.producer.produce(topic, value=json.dumps(message).encode('utf-8'), callback=self.delivery_report)
        self.producer.flush()
