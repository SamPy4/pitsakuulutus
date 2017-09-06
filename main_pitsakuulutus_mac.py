import paho.mqtt.client as mqtt


""" MQTT EI TULE TOIMIMAAN !!!!! """
class mac():
    def __init__(self):
        self.port = 1883
        self.path = "pitsatilaus123"

        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        self.client.connect("iot.eclipse.org", self.port, 60)

        self.step = 1 # Loop step

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

        self.client.subscribe(self.Path + "/#")

    def on_message(self, client, userdata, msg):
        topic = msg.topic # The name of variable. For example path/button1 that variable name is button1
        value = msg.payload # The sent value


    # The main loop
    def run(self):
        while True:
            self.client.loop()

            time.sleep(self.step) # looping the mqtt protocol step amount of seconds

if __name__ == "__main__":
    main = rasberry()
    main.run()
