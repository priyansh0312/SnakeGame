import pygame 
import time
import random
import math 


# making a food object 
class Food:

	def __init__(self,xspeed,yspeed,scale,width,height):
		self.scale = scale
		self.height = height 
		self.width = width
		self.xspeed = xspeed
		self.yspeed = yspeed 
		self.foodx = round(random.randrange(0,self.width-self.scale) / 10.0)* 10.0
		self.foody = round(random.randrange(0,self.height-self.scale) / 10.0)* 10.0
	
	
	# creating the food block
	def makeFood(self,color,surface):
		pygame.draw.rect(surface,color,[self.foodx,self.foody,self.scale,self.scale])


	# checing if the food is eaten by snake or not
	def isEaten(self,x,y,total):
		if x == self.foodx and y == self.foody:
			self.foodx = round(random.randint(0,self.width-self.scale) / 10.0) * 10.0
			self.foody = round(random.randint(0,self.height-self.scale) / 10.0) * 10.0
			return total+1
		return total