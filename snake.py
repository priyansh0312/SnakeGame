import pygame 
import time
import random
import math 


# making a Snake Object
class Snake:
	def __init__(self,height,width,scale):
		self.scale = scale
		self.height = height 
		self.width = width


	def createSnake(self,x,y,head,body,total,color,surface):
		head.append(x)
		head.append(y)
		body.append(head)

		if len(body)>total:
			del body[0]

		# creating snake blocks 
		for i in body:
			pygame.draw.rect(surface,color,[i[0],i[1],self.scale,self.scale])

		return body,head


	# checking collision with itself
	def checkSelf(self,gameOver,head,body):
		for i in body[:-1]:
			if i == head:
				gameOver = True
		return gameOver
	

	# assigning directions to the snake 
	def direction(self,speed,event,xspeed,yspeed):
		if event.type == pygame.KEYDOWN :
			if event.key == pygame.K_LEFT:
				xspeed = -speed
				yspeed = 0
			if event.key == pygame.K_RIGHT:
				xspeed = speed
				yspeed = 0
			if event.key == pygame.K_DOWN:
				xspeed = 0
				yspeed = speed
			if event.key == pygame.K_UP:
				xspeed = 0
				yspeed = -speed
		return xspeed,yspeed


	# checking collison with the boundaries
	def checkBoundaries(self,x,gameOver,y):
		if x>=self.width or x<0 or y>=self.height or y<0:
			gameOver = True
		return gameOver
		



