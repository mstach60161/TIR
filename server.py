import json
import paho.mqtt.client as mqtt
from datetime import datetime


def load_panel_data(data):
    # for k in range(len(data['I'])):
    print(data['I'], data['V'], data['G'], data["S"], data['Time'])
    print("Panel name: " + data["panel_name"])


def on_message(client, userdata, msg):
    data = msg.payload.decode("utf-8")
    # print("received: " + msg.topic + " " + data)
    if "from_panel" in msg.topic:
        # print(data)
        load_panel_data(json.loads(data))
    else:
        print("Unavailable command: " + msg.topic)


def on_connect(client, userdata, flags, rc):
    print("server started")
    mqttc.subscribe("data/from_panel/#")  # odbieranie wiadomosci od paneli


mqttc = mqtt.Client("server")
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.connect("test.mosquitto.org", 1883, 60)

mqttc.loop_forever()
