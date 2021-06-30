import pyautogui
from datetime import datetime
from time import sleep
import sys
import keyboard
import random

path = ""
counter = 0

with open("path.txt") as f:
	path = f.read()

def screenshot():
	global counter
	myScreenshot = pyautogui.screenshot()
	myScreenshot.save(path + '\\' + str(datetime.now().day) + '-ое число, [' + str(datetime.now().hour) + '-' + str(datetime.now().minute) + '] [' + str(random.randint(100, 1000)) + '].png')
	print("Saved!")
	print("Screenshot count: " + str(counter))
	counter += 1

while True:
	keyboard.add_hotkey('Ctrl + 2', screenshot())
	try:
		keyboard.wait('Ctrl + Q')
	except Exception as e:
		print(e)

