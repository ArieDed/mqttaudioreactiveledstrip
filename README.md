# mqttaudioreactiveledstrip

Simple MQTT Python 3 script to work together with [Audio-reactive-led-strip](https://github.com/Aircoookie/audio-reactive-led-strip). Change the following variables in the script:

* MQTT_IP_ADRESS: The ip address of your mqtt server
* MQTT_PORT: The port of your mqtt server
* MQTT_USERNAME: Your mqtt server username
* MQTT_PASSWORD: The password of your mqtt server and username

You could also change the led_strip/music the mqtt client listens on. Install the paho-mqtt client module for python to make it work. 

I have this running on a small Ubuntu server VM and connected to a Mosquitto mqtt on home assistant to turn on the audio reactive led strip using home assistant quickly and easily. Put the mqtt file together with the  [Audio-reactive-led-strip](https://github.com/Aircoookie/audio-reactive-led-strip) files and run the mqtt script in the background using nohup.
