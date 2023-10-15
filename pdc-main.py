# Python-based digital clock
# Author: xoiioi
from datetime import datetime # pip install datetime
from art import * # pip install art
import time
import os

delay = 0.9 # Clock delay
while True:
	now = datetime.now()
	timenow = now.strftime("%H:%M")
	timeart=text2art(timenow, font='big')
	print(timeart)
	time.sleep(delay) # Delay
	os.system('clear') # Clear console
 
