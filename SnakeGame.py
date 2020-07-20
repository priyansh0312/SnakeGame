import pygame
import snake
import time 

# initializing the pygame module 
pygame.init()

# dimensions of the surface:
width = 900
height = 700
resolution = (width,height)
FPS = 20

# pygame.display.update()
surface = pygame.display.set_mode(resolution) #setting the screen resolution 
pygame.display.set_caption("Snake it!")
clock = pygame.time.Clock()


# defining the colors :
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (0, 0, 128)

# pixel density index :
scale = 15
speed = 10


font = pygame.font.Font('freesansbold.ttf',20)


# for displaying message
def message(msg,color1,color2,surface):
	mesg = font.render(msg,True,color1,color2)
	rect = mesg.get_rect()
	rect.center = (width//2,height//2)
	surface.blit(mesg,rect) 


def score(score):
    value = font.render("Your Score: " + str(score), True, yellow)
    surface.blit(value,[0, 0])



# running state of the game :
def gameRunning():

	running = True 
	gameOver = False
	x = width/2
	y = height/2
	xspeed = 0
	yspeed = 0

	body = []
	total = 1

	Snake = snake.Snake(height,width,scale)
	Food = snake.Food(xspeed,yspeed,scale,width,height)


	while running :

		clock.tick(15)
		surface.fill(black)
		
		if gameOver:
			surface.fill(black)
			message("OOPS, YOU LOST! Press SPACE-Restart or ESC-Exit",red,blue,surface)
			score(total-1)
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						running = False
					if event.key == pygame.K_SPACE:
						gameRunning()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False 
			xspeed,yspeed = Snake.direction(speed,event,xspeed,yspeed)

		gameOver =  Snake.checkBoundaries(x,gameOver,y)
			
		x+=xspeed
		y+=yspeed

		Food.makeFood(red,surface)
		
		head = []
		body,head = Snake.createSnake(x,y,head,body,total,white,surface)
		gameOver = Snake.checkSelf(gameOver,head,body)
		score(total-1)

		pygame.display.update()

		total = Food.isEaten(x,y,total)
		Food.makeFood(green,surface)
			

	pygame.quit()
	quit()

gameRunning()









