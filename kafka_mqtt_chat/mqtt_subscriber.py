import paho.mqtt.client as mqtt
import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO)

# MQTT Broker details
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "test/topic"


# Callback for logging the successful connection
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logging.info("Connected to MQTT Broker successfully")
        # Subscribe to the topic inside the on_connect callback
        client.subscribe(MQTT_TOPIC)
    else:
        logging.error(f"Failed to connect, return code {rc}")


# Callback when a message is received
def on_message(client, userdata, msg):
    logging.info(
        f"Received message: {msg.payload.decode()} on topic {msg.topic}"
    )


# Initialize MQTT Client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# Assign the callbacks to the client
client.on_connect = on_connect
client.on_message = on_message

try:
    # Connect to the broker
    client.connect(MQTT_BROKER, MQTT_PORT, 60)

    # Start the loop to process network traffic and dispatch callbacks
    client.loop_forever()
except Exception as e:
    logging.error(f"An error occurred: {e}")
