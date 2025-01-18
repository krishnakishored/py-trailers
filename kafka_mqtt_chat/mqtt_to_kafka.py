"""
Publisher:
This script acts as an MQTT client that publishes chat messages, which are then forwarded to a Kafka topic.
Improved with error handling and debugging.
"""

import paho.mqtt.client as mqtt
from kafka import KafkaProducer
import json
import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO)

# MQTT and Kafka configuration
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "chatroom/general"

KAFKA_BROKER = "10.10.15.35:9092"
KAFKA_TOPIC = "mqtt_chat"


# Initialize Kafka producer with error handling
def create_kafka_producer():
    try:
        producer = KafkaProducer(
            bootstrap_servers=KAFKA_BROKER,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )
        return producer
    except Exception as e:
        logging.error(f"Failed to create Kafka producer: {e}")
        raise


producer = create_kafka_producer()


# MQTT on_connect callback
# def on_connect(client, userdata, flags, rc):
def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        logging.info("Connected to MQTT Broker!")
        client.subscribe(MQTT_TOPIC)
    else:
        logging.error(
            f"Failed to connect to MQTT Broker, return code {reason_code}"
        )


# MQTT on_message callback
def on_message(client, userdata, msg):
    message = msg.payload.decode()
    logging.info(f"Received message: {message}")
    try:
        future = producer.send(
            KAFKA_TOPIC, {"topic": msg.topic, "message": message}
        )
        result = future.get(timeout=10)  # Wait for send confirmation
        logging.info(f"Message sent to Kafka topic {KAFKA_TOPIC}")
    except Exception as e:
        logging.error(f"Failed to send message to Kafka: {e}")


# Initialize MQTT client with callbacks
mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

# Connect to MQTT broker
try:
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
except Exception as e:
    logging.error(f"Failed to connect to MQTT Broker: {e}")
    exit(1)

# Start the MQTT loop
mqtt_client.loop_start()

# Keep the script running
try:
    while True:
        pass
except KeyboardInterrupt:
    logging.info("Script terminated by user")
finally:
    mqtt_client.loop_stop()
    mqtt_client.disconnect()
    logging.info("MQTT client disconnected")
