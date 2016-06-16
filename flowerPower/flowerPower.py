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
import RPi.GPIO as gpio

__version__ = 0.1
__author__ = 'Atle Krogstad Berg - mail@atleberg.com'



## APPLICATION ##

def main():
	currentPath = os.path.dirname(os.path.abspath(sys.argv[0]))

	print gpio.RPI_INFO

	gpio.setmode(gpio.BCM)

if (__name__ == "__main__"):
	main()
