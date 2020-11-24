#!/usr/bin/env python
#2020/11/24 Radosław Michoń - Simple pulse generator v0.1 for pigpiod library

import time
import pigpio

port=16
dc=64

pi = pigpio.pi()
pi.set_PWM_dutycycle(port,dc)

if not pi.connected:
   exit()

print("Sending pulses to GPIO "+str(port)+", control+C to stop.")

while True:
   try:
      speed=100
      speed=(speed*12)
      pi.set_PWM_frequency(port,speed)
      time.sleep(1)

   except KeyboardInterrupt:
       print("\nTidying up")
       pi.set_PWM_frequency(port,0)
       break

pi.stop()
