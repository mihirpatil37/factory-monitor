import paho.mqtt.client as mqtt
from database import init_db, save_reading

def on_message(client, userdata, message):
    topic = message.topic
    value = message.payload.decode()
    save_reading(topic, value)
    print(f"[{topic}] → {value}")

init_db()

broker = "broker.hivemq.com"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message
client.connect(broker, 1883)

client.subscribe("factory/line1/machine1/#")

print("Listening and saving to database...")
client.loop_forever()