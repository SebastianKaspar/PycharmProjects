#Import
import RPi.GPIO as GPIO
import time
import datetime
import picamera
import os
 
datapath = '/home/pi/PycharmProjects/Bewegungsmelder'

print "~BEWEGUNGSMELDER~"
print ""
 
#Board Mode: Angabe der Pin-Nummer
GPIO.setmode(GPIO.BOARD)
 
#GPIO Pin definieren fuer den Dateneingang vom Sensor
PIR_GPIO =8 
GPIO.setup(PIR_GPIO,GPIO.IN)
 
read=0
wait=0
 
try:  
 #PIR auslesen
 while GPIO.input(PIR_GPIO)==1:
   read=0
 print "WARTEN auf Bewegung..."
 
 #Abbruch ctrl+c
 i=0
 while True : 
   #PIR auslesen
   read = GPIO.input(PIR_GPIO)
   
   if read==1 and wait==0: 
     print "ALARM %s: Bewegung erkannt!" % datetime.datetime.now() 
     global camera
     with picamera.PiCamera() as camera:
        camera.start_preview()
        camera.capture_sequence([os.path.join(datapath, 'Alarm' +str(datetime.datetime.now()))+'.png' ])
     wait=1
 
   elif read==0 and wait==1: 
     print "WARTEN auf Bewegung..." 
     wait=0
 
 time.sleep(0.01)
 
except KeyboardInterrupt:
 print "Beendet"
 GPIO.cleanup()
