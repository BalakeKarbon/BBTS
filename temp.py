#! /usr/bin/env python

import json
import math
import Adafruit_BBIO.ADC as ADC
from time import sleep

ADC.setup()

samples=[]
for i in range(100):
	samples.append(1)

for x in range(0,100):
	samples[x]=ADC.read("P9_40")
	sleep(0.001)

average=0

for x in range(0,100):
	average=average+samples[x]

value = average / 100
volts = value * 1.8
ohms = 5000/(volts/(3.33-volts))

lnohm = math.log1p(ohms)

#a, b, & c values from http://www.thermistor.com/calculators.php
#using curve R (-6.2%/C @ 25C) Mil Ratio X
a =  0.001834324240068
b =  0.000157235894316
c =  0.000000090965379

#Steinhart Hart Equation
# T = 1/(a + b[ln(ohm)] + c[ln(ohm)]^3)

t1 = (b*lnohm) # b[ln(ohm)]

c2 = c*lnohm # c[ln(ohm)]

t2 = math.pow(c2,3) # c[ln(ohm)]^3

temp = 1/(a + t1 + t2) #calcualte temperature

tempc = temp - 273.15 - 4 #K to C
# the -4 is error correction for bad python math

tempcc = tempc - 3

f = open('/var/lib/cloud9/parnode/BBB2.json', 'w')
json_map = {}
json_map["Ambient"] = tempcc
json.dump(json_map, f)

print(str(tempcc))
