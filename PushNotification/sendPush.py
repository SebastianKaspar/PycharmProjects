import pynma
import os

if os.path.isfile("myapikey"):
        apikey = open("myapikey",'r').readline().strip()
p = pynma.PyNMA(apikey)

p.push("System: Pi", "Event: tbd", "Hi! This is my first test to send a push message...")
