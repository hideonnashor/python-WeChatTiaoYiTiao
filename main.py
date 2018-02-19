import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import time



def pullScreenshot():
	os.system('adb shell screencap /sdcard/some.png')
	os.system('adb pull /sdcard/some.png E:/PythonSpace/awesome-wechatTiaoYITiao/some.png')

def jump(distance):
	onPressTime = int(distance * 1.35)
	string = str(onPressTime)
	cmd = 'abd shell input swipe 320 410 320 410'+str(string)
	print(cmd)
	os.system(cmd)

fig = plt.figure()
index = 0
cor = [0,0]

pullScreenshot()
img = np.array(Image.open('some.png'))

update = True
clickCount = 0
cor = []

def updateImg():
	return np.array(Image.open('some.png'))

im = plt.imshow(img,animated = True)

def updatefig(*args):
	global update
	if update:
		time.sleep(1.5)
		pullScreenshot()
		im.set_array(updateImg())
		update = False
	return im

def onClick(event):
	global update
	global ix,iy
	global clickCount
	global cor

	ix,iy = event.xdata,event.ydata
	coords = []
	coords.append((ix,iy))
	print('now = ',coords)
	cor.append(coords)

	clickCount += 1
	if clickCount > 1:
		clickCount = 0

		cor1 = cor.pop()
		cor2 = cor.pop()

		distance = (cor1[0][0] - cor2[0][0])**2 + (cor1[0][1] - cor2[0][1])**2
		distance = distance ** 0.5
		print('distance = ',distance)
		jump(distance)
		update = True

fig.canvas.mpl_connect('button_press_event',onClick)
ani = animation.FuncAnimation(fig,updatefig,interval = 50,blit = True)

plt.show()

 


