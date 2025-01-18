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
    else:
        logging.error(f"Failed to connect, return code {rc}")


# Callback for logging the successful message publishing
def on_publish(client, userdata, mid):
    logging.info("Message Published successfully")


# Initialize MQTT Client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# Assign the callbacks to the client
client.on_connect = on_connect
client.on_publish = on_publish

try:
    # Connect to the broker
    client.connect(MQTT_BROKER, MQTT_PORT, 60)

    # Start the loop
    client.loop_start()

    # Publish a message
    (rc, mid) = client.publish(MQTT_TOPIC, "Hello, MQTT!")
    if rc == mqtt.MQTT_ERR_SUCCESS:
        logging.info("Publishing message")
    else:
        logging.error("Failed to publish message")

    # Stop the loop
    client.loop_stop()

    # Disconnect from the broker
    client.disconnect()
    logging.info("Disconnected from MQTT Broker")
except Exception as e:
    logging.error(f"An error occurred: {e}")
