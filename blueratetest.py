import random
import time
import atexit
import math
import numpy
from PIL import Image
from PIL import ImageDraw

def ratecalcsin(step,scale):
	return int(round(255*math.sin(math.radians(90*(step/scale)))))

class sun:
	def __init__(self,panelno):
		self.color = (0,0,0)
		self.panel = panelno
		self.location = [0,0,0,0]
		self.step = 0 #so each sun can track its own state
		self.maxstep = 109
		#this bit is basically a conviluted way to initialize where the sun is (if it's sun 0 spawn in panel 0, ect)
		if self.panel == 0:
			self.location = [0,0,31,31]
		elif self.panel == 1:
			self.location = [32,0,64,32]
		else:
			self.location = [0,0,0,0]
	def colorinc(self):
		#print 'self.step is:'
		#print self.step
		if self.step == self.maxstep:
			pass
		elif self.step >= 0 and self.step < self.maxstep:
			self.step += 1
			#this whole line is basically to try to make a non-linear scale of light
			#intent is to go from a steeper change value at the beginning to a more gradual one later
			#super conviluted but it's the best I could think of at the time
			#colorval = int(round(255*math.sin(math.radians((90*(self.step/self.maxstep))))))
			# this is a shitty hack to make it get gradually more yellow
			colorvalr = ratecalcsin(float(self.step),self.maxstep)
			colorvalg = int(float(self.step)/self.maxstep*255)
			if self.step > int(float(self.maxstep)/4):
				colorvalb = int(float(self.step-int(float(self.maxstep)/4))/self.maxstep*255)
			else: 
				colorvalb = 0
			if colorvalb < 256 and colorvalr < 256 and colorvalg < 256:
				self.color = (colorvalr,colorvalg,colorvalb)
				print self.color
			else:
				pass
	def draw(self):
		draw.rectangle((self.location), fill=self.color)
poop = 0 
sunrise_lw = sun(0)
while poop < 200:
	
	poop += 1
	print "poop is:"
	print poop
	sunrise_lw.colorinc()