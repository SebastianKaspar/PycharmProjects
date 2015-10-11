"""
Created on Sat Oct 10 15:48:59 2015

@author: Sebastian Kaspar
"""

import urllib2
import sys
import json
import numpy as np
import pynma
import os

reload(sys)
sys.setdefaultencoding("utf-8")

pushMessageString = ""
shares = {}
with open("/home/pi/PycharmProjects/Aktienkurse/myShares.txt") as jsondict:
    shares = json.load(jsondict)

print "Downloading current stocks..."
for key in sorted(shares):
    url = urllib2.urlopen(shares[key]["url"])
    with open("/var/tmp"+key+".txt", 'w') as f:
        i=0    
        for line in url:
            if line.find("itemprop="+"\""+"price")>=0:
                try:
                    start = str(line).index("itemprop="+"\""+"price")+17
                    if key not in ["CHFzuEUR"]:
                        end = str(line).index("&nbsp;&euro;<")
                    else:
                        end = str(line).index("</span")
                    aktuellerKurs = round(float(line[start:end].replace(",",".")),2)
                    change = round((aktuellerKurs - shares[key]["Kaufkurs"])*shares[key]["Anteile"],2)
                    if change < 0:
                        pm = ""
                    else:
                        pm = "+"
                    percentChange = np.abs((aktuellerKurs-shares[key]["Kaufkurs"])/shares[key]["Kaufkurs"])  
                    if 0.15 < percentChange:
                        message = "> "+str(key), aktuellerKurs, str(pm)+str(change)                     
                    else:
                        message = "  "+str(key), aktuellerKurs, str(pm)+str(change)
                    pushMessageString+=str(message)
                    pushMessageString+="\n"
                except:
                    print "Price not found! Check script."
            f.write(line)
print pushMessageString

if os.path.isfile("/home/pi/PycharmProjects/PushNotification/myapikey"):
        apikey = open("/home/pi/PycharmProjects/PushNotification/myapikey",'r').readline().strip()
p = pynma.PyNMA(apikey)
p.push("System: Pi", "Event: Boersenmonitor", str(pushMessageString))
print "Push notificarion sent"


