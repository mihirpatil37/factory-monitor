import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    topic = message.topic
    value = message.payload.decode()
    print(f"[{topic}] → {value}")

broker = "broker.hivemq.com"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message
client.connect(broker, 1883)

client.subscribe("factory/line1/#")

print("Listening for messages...")
client.loop_forever()