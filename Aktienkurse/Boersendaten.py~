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


def get_path():
    path = os.path.dirname(os.path.abspath(__file__))
    return path


pushMessageString = ""
shares = {}
mainpath = get_path()
with open(os.path.join(mainpath, "myShares.txt")) as jsondict:
    shares = json.load(jsondict)


print "Downloading current stocks..."
for key in sorted(shares):
    url = urllib2.urlopen(shares[key]["url"])
    letters = len(key)
    points2add = ""
    for i in range(15-letters):
        points2add += "."

    with open(os.path.join("/var/tmp", key + ".txt"), 'w') as f:
        for line in url:
            if line.find("itemprop=" + "\"" + "price") >= 0:
                try:
                    start = str(line).index("itemprop=" + "\"" + "price") + 17
                    if key not in ["CHFzuEUR"]:
                        end = str(line).index("&nbsp;&euro;<")
                    else:
                        end = str(line).index("</span")
                    aktuellerKurs = round(float(line[start:end].replace(",", ".")), 4)
                    points2add2 = ""
                    for i in range(9-len(str(aktuellerKurs))):
                        points2add2 += "."
                    change = round((aktuellerKurs - shares[key]["Kaufkurs"]) * shares[key]["Anteile"], 2)
                    if change < 0:
                        pm = ""
                    else:
                        pm = "+"
                    percentChange = np.abs((aktuellerKurs - shares[key]["Kaufkurs"]) / shares[key]["Kaufkurs"])
                    if 0.15 < percentChange:
                        message = ">" + str(key) + ": " + str(points2add) + str(aktuellerKurs) + ", " + str(points2add2) + str(pm) + str(change)
                    else:
                        message = "_" + str(key) + ": " + str(points2add) + str(aktuellerKurs) + ", " + str(points2add2) + str(pm) + str(change)
                    pushMessageString += str(message)
                except:
                    print "Price not found! Check script."
            if key in ["CHFhighRisk", "CHFlowRisk", "DaxKO"]:
                if line.find("Einfacher Hebel</td") >= 0:
                    try:
                        start = str(line).index("Einfacher Hebel</td> <td class") + 38
                        end = str(line).index(" </td> </tr> <tr> <td class=") - 1
                        hebel = round(float(line[start:end].replace(",", ".")), 2)
                        pushMessageString += ", [" + str(hebel) + "]"
                    except:
                        print "Error reading Hebel"
            f.write(line)
    pushMessageString += "\n"
print pushMessageString

if os.path.isfile(os.path.join(mainpath, "myapikey")):
    apikey = open(os.path.join(mainpath, "myapikey"), 'r').readline().strip()
p = pynma.PyNMA(apikey)
p.push("System: Pi", "Event: Boersenmonitor", str(pushMessageString))
print "Push notification sent"


