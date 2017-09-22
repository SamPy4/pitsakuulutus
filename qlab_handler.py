#from pythonosc import osc_message_builder
#from pythonosc import udp_client
#from pyautogui import typewrite
from time import sleep
import argparse, os

# parser = argparse.ArgumentParser()
#
# parser.add_argument("--ip", default="10.1.184.189",
#       help="The ip of the OSC server")
#
# parser.add_argument("--port", type=int, default=53001,
#       help="The port the OSC server is listening on")
#
# args = parser.parse_args()
#
# client = udp_client.SimpleUDPClient(args.ip, args.port)
#
# client.send_message("/address", "GO")

def qlab_GO():
    print("Painampa koota")
    #typewrite("k")
    #os.system("vlc pitsa-audio.mpeg vlc://quit")
    return

if __name__ == "__main__":
    sleep(0)
    qlab_GO()
