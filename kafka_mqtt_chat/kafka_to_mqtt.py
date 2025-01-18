"""
Subscriber:
This script subscribes to Kafka messages and forwards them to an MQTT topic, allowing all clients to receive the message.
Improved with error handling and debugging.
"""

import paho.mqtt.client as mqtt
from kafka import KafkaConsumer
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


# MQTT on_connect callback
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logging.info("Connected to MQTT Broker!")
    else:
        logging.error(f"Failed to connect to MQTT Broker, return code {rc}")
        exit(1)  # Exit if connection failed


# Initialize MQTT client with Version 2 Callback API
mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqtt_client.on_connect = on_connect

# Connect to MQTT broker
try:
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
    mqtt_client.loop_start()  # Start the loop to process callbacks
except Exception as e:
    logging.error(f"Failed to connect to MQTT Broker: {e}")
    exit(1)

# Initialize Kafka consumer with error handling
try:
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BROKER,
        value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    )
except Exception as e:
    logging.error(f"Failed to create Kafka consumer: {e}")
    exit(1)

# Process messages from Kafka and publish to MQTT
try:
    for message in consumer:
        data = message.value
        mqtt_message = f"[{data['topic']}] {data['message']}"
        result = mqtt_client.publish(MQTT_TOPIC, mqtt_message)
        # Check if publish was successful
        if result.rc != mqtt.MQTT_ERR_SUCCESS:
            logging.error(f"Failed to publish message to MQTT: {mqtt_message}")
        else:
            logging.info(f"Sent message: {mqtt_message}")
except KeyboardInterrupt:
    logging.info("Script terminated by user")
finally:
    mqtt_client.loop_stop()
    mqtt_client.disconnect()
    logging.info("MQTT client disconnected")
