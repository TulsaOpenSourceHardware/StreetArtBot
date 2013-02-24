#!/usr/bin/env python
import tuio, pygame
import observer

from chalkboard import ChalkBoard

image = "images/fab.jpg"

#Creates the pygame screen
width, height = (120, 90)

board = ChalkBoard()
width, height = board.loadImage(image, width, height)
size = (width, height)
size_multi = 3
bloated = (width*size_multi, height*size_multi)

screen = pygame.display.set_mode(bloated)
# screen.fill((255, 255, 255))
background = pygame.image.load(image)
print background.get_size()
backgroundrect = background.get_rect()

screen.blit(background, backgroundrect)

class Listener(observer.AbstractListener):
	#Implements a Listener
	def notify(self, event):
		# Shows a square, on the appropriate coordinates
		point = pygame.Surface((size_multi, size_multi))
		screen.blit(point, ((int(bloated[0]*event.object.xpos)), (int(bloated[1]*event.object.ypos))))
		pygame.display.update()

listener = Listener("Event Listener", tuio.getEventManager())
tuio.mainLoop()

        