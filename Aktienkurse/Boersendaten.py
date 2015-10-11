"""
Created on Sat Oct 10 15:48:59 2015

@author: Sebastian Kaspar
"""

import urllib2
import sys
import json

reload(sys)
sys.setdefaultencoding("utf-8")

shares = {}
with open("/home/pi/PycharmProjects/Aktienkurse/myShares.txt") as jsondict:
    shares = json.load(jsondict)

for key in sorted(shares):
    url = urllib2.urlopen(shares[key]["url"])
    with open("/home/pi/PycharmProjects/Aktienkurse/Daten/"+key+".txt", 'w') as f:
        i=0    
        for line in url:
            if line.find("itemprop="+"\""+"price")>=0:
                try:
                    start = str(line).index("itemprop="+"\""+"price")+17
                    if key not in ["CHFzuEUR"]:
                        end = str(line).index("&nbsp;&euro;<")
                    else:
                        end = str(line).index("</span")
                    print key, line[start:end]
                except:
                    print "Price not found! Check script."
            f.write(line)

