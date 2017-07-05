#!/usr/bin/env python3
# author Rajeev

import webbrowser,time
import pyautogui

url = input("Enter the url for downloading: ")
n = int(input("Number of episodes to be downloaded: "))
print("Press Ctrl+C to stop")
webbrowser.open(url)
try:
	for i in range( 0, n ):
			while True: 
				if ( pyautogui.locateOnScreen( "download.png" ) != None ):
					downloadbutton = pyautogui.locateOnScreen( "download.png" )
					b1, b2 = pyautogui.center( downloadbutton )
					pyautogui.moveTo( b1, b2, duration = 0.50 )
					pyautogui.click( b1, b2 )
					time.sleep(1.25)
					# The values in moveTo() & click() are X and Y coordinates of the screen.
					# Change the values according to your screen resolution.
					# Values in this code are for screens with resolution 1366 x 768.
					# You can change the value of duration according to your needs but try not to make it zero(system may hang).
					pyautogui.moveTo( 1355, 95, duration = 1 )
					pyautogui.click( 1355, 95, clicks = 1 )
					time.sleep(0.25)
					if(pyautogui.locateOnScreen( "next.png" ) != None ):
						nextbutt = pyautogui.locateOnScreen( "next.png" )
						butt1,butt2 = pyautogui.center( nextbutt )
						pyautogui.moveTo( butt1, butt2, duration = 0.65 )
						pyautogui.click( butt1, butt2 )
						break
except KeyboardInterrupt:
	print ( "Automatic Downloading Stopped" )
