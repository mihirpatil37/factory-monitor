import time
import random
import paho.mqtt.client as mqtt

# Connect to public broker
broker = "broker.hivemq.com"
topic_temp = "factory/line1/machine1/temperature"
topic_pressure = "factory/line1/machine1/pressure"
topic_status = "factory/line1/machine1/status"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(broker, 1883)

print("Connected to MQTT broker. Publishing data...")

while True:
    temperature = round(random.uniform(60.0, 90.0), 2)
    pressure = round(random.uniform(1.0, 5.0), 2)
    status = random.choice(["RUNNING", "STOPPED"])

    client.publish(topic_temp, temperature)
    client.publish(topic_pressure, pressure)
    client.publish(topic_status, status)

    print(f"Temperature : {temperature} °C")
    print(f"Pressure    : {pressure} bar")
    print(f"Status      : {status}")
    print("---")
    time.sleep(2)