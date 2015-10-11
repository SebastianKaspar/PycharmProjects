"""
Created on Sat Oct 10 15:48:59 2015

@author: Sebastian Kaspar
"""

import urllib2
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

shares = {"FranklinMena": "http://www.ariva.de/franklin_mena_fund_a(acc)_eur-fonds?utp=1",
                 "CHFhighRisk": "http://www.ariva.de/VZ8XR2?utp=1",
                  "CHFlowRisk": "http://www.ariva.de/CR74M2?utp=1",
                  "DaxKO":"http://www.ariva.de/VS3T3V?utp=1",
                  "BOVESPA": "http://www.ariva.de/lyxor_etf_brazil_ibovespa-fonds?utp=1",
                  "Nordea": "http://www.ariva.de/stable_return_fund_bp_eur-fonds?utp=1",
                   "HausInvest": "http://www.ariva.de/hausinvest-fonds?utp=1",
                   "WertGrund": "http://www.ariva.de/wertgrund_wohnselect_d-fonds?utp=1",
                   "LeadingCities": "http://www.ariva.de/leading_cities_invest-fonds?utp=1/"
                    }

for key in sorted(shares):
    url = urllib2.urlopen(shares[key])
    with open("/home/pi/PycharmProjects/Aktienkurse/Daten/"+key+".txt", 'w') as f:
        i=0    
        for line in url:
            if line.find("itemprop="+"\""+"price")>=0:
                try:
                    start = str(line).index("itemprop="+"\""+"price")+17
                    end = str(line).index("&nbsp;&euro;<")
                    print key, line[start:end]
                except:
                    print "Price not found! Check script."
            f.write(line)
