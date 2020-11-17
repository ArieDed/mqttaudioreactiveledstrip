#!/usr/bin/python3

import paho.mqtt.client as mqtt
import subprocess as sp
import re

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    #print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("led_strip/#")

# The callback for when a PUBLISH message is received from the server.
def on_music(client, userdata, msg):
    msg.payload = msg.payload.decode("utf-8")
    print(msg.topic+" "+str(msg.payload))
    if msg.payload == "ON":
        global p
        p = sp.Popen(['python3', 'visualization.py'])
    if msg.payload == "OFF":
        try:
            p.terminate()
            print("terminating...")
        except:
            pass
#        import config
#        import socket
#        _sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#        o = []
#        p = [0, 0, 0]
#        a = range(1,91)
#        for i in a:
#            o.append(i)
#            o.append(p[0])
#            o.append(p[1])
#            o.append(p[2])
#        o = bytes(o)
#        _sock.sendto(o, (config.UDP_IP, config.UDP_PORT))

#def on_light(client, userdata, msg):
#    msg.payload = msg.payload.decode("utf-8")
#    print(msg.topic+" "+str(msg.payload))    
#    if msg.payload == "ON":
#        try:
#            p.terminate()
#        except:
#            pass
#        import config
#        import socket
#        _sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#        o = []
#        try:
#            b = [bright, bright, bright]
#        except:
#            b = [255, 255, 255]
#        try:
#            rgb_values = [int(color[0]), int(color[1]), int(color[2])]
#            p = [int(b[0]/255*rgb_values[0]), int(b[1]/255*rgb_values[1]), int(b[2]/255*rgb_values[2])]
#        except:
#            p = [b[0], b[1], b[2]]
#        a = range(1,91)
#        for i in a:
#            o.append(i)
#            o.append(p[0])
#            o.append(p[1])
#            o.append(p[2])
#        o = bytes(o)
#        _sock.sendto(o, (config.UDP_IP, config.UDP_PORT))
#    if msg.payload == "OFF":
#        print("Clearing led strip")
#        try:
#            p.terminate()
#        except:
#            pass
#        import config
#        import socket
#        _sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#        o = []
#        p = [0, 0, 0]
#        a = range(1,91)
#        for i in a:
#            o.append(i)
#            o.append(p[0])
#            o.append(p[1])
#            o.append(p[2])
#        o = bytes(o)
#        _sock.sendto(o, (config.UDP_IP, config.UDP_PORT))
#        
#def on_brightness(client, userdata, msg):
#    msg.payload = msg.payload.decode("utf-8")
#    global bright
#    print(msg.topic+" "+str(msg.payload))
#    bright = int(msg.payload)
#        
#def on_rgb(client, userdata, msg):
#    msg.payload = msg.payload.decode("utf-8")
#    global color
#    print(msg.topic+" "+str(msg.payload))
#    color = msg.payload
#    color = re.findall('\d+', color)

client = mqtt.Client("LED_strip_music")
client.username_pw_set(username="MQTT_USERNAME",password="MQTT_PASSWORD")
client.on_connect = on_connect
client.message_callback_add('led_strip/music', on_music)
#client.message_callback_add('led_strip/light/on', on_light)
#client.message_callback_add('led_strip/light/brightness', on_brightness)
#client.message_callback_add('led_strip/light/RGB', on_rgb)

#client.on_message = on_message

client.connect("MQTT_IP_ADRESS", MQTT_PORT)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
