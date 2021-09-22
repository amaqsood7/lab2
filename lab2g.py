#!/usr/bin/env python3


#Author: Ahmed Maqsood
#AUthor ID: 132779190
#Date: 9/22/2021

import sys

if len(sys.argv) == 1:
	timer = 3
else:
	timer = int(sys.argv[1])
while timer != 0:
	print(timer)
	timer = timer - 1
print('blast off!')
