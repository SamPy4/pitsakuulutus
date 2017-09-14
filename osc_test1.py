from pythonosc import osc_message_builder
from pythonosc import udp_client

import argparse



parser = argparse.ArgumentParser()

parser.add_argument("--ip", default="10.1.184.189",
      help="The ip of the OSC server")

parser.add_argument("--port", type=int, default=53000,
      help="The port the OSC server is listening on")

args = parser.parse_args()

client = udp_client.SimpleUDPClient(args.ip, args.port)

client.send("cue/2/start","")
