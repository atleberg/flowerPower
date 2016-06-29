#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# flowerPower main Python app
# Copyright 2015 Atle Krogstad Berg (mail@atleberg.com)
#

from config import *
import os
import sys
import time
import logging
import RPi.GPIO as GPIO

__version__ = 0.1
__author__ = 'Atle Krogstad Berg - mail@atleberg.com'



## APPLICATION ##

def main():
	currentPath = os.path.dirname(os.path.abspath(sys.argv[0]))

	print GPIO.RPI_INFO

	motors = dict()

	GPIO.setmode(GPIO.BCM)
	for currentPin in FP_PIN_CONFIG:
		GPIO.setup(currentPin, GPIO.OUT)
		GPIO.output(currentPin, False)

		#pwm = GPIO.PWM(currentPin, 500)
		#pwm.start(100)

	newPwm(50) # 0 - 100
	pwm.ChangeDutyCycle(float(newPwm))

	# Turn on
	#GPIO.output(currentPin, False)


if (__name__ == "__main__"):
	main()
