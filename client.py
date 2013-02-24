#!/usr/bin/env python
import tuio, pygame
import observer

from utils import trace
from chalkboard import ChalkBoard

image = "images/fab.jpg"

#list of fiducials to track
track_fiducials = [0,1,2,3,4]

#Creates the pygame screen
width, height = (120, 90)

board = ChalkBoard(port="/dev/tty.usbmodem1421") #port="/dev/tty.RN42-4FB7-SPP"
width, height, im = board.loadImage(image, width, height)
size = (width, height)
size_multi = 3
bloated = (width*size_multi, height*size_multi)
bloated_image = im.resize(bloated)
screen = pygame.display.set_mode(bloated)
# fill white
# screen.fill((255, 255, 255))
bloated_image.save('images/bloated.jpg')
background = pygame.image.load('images/bloated.jpg')
print background.get_size()
backgroundrect = background.get_rect()

screen.blit(background, backgroundrect)
pygame.display.update()

tracking = tuio.Tracking()

class Listener(observer.AbstractListener):
	#Implements a Listener
	def notify(self, event):
		# if not event.object.id in track_fiducials:
		# 	return
		# Shows a square, on the appropriate coordinates
		
		point = pygame.Surface((size_multi, size_multi))
		screen.blit(point, ((int(bloated[0]*event.object.xpos)), (int(bloated[1]*event.object.ypos))))
		pygame.display.update()
		
		board.checkSpray(event.object.xpos, event.object.ypos, event.object.id)

listener = Listener("Event Listener", tracking.eventManager)

def mainLoop():
    try:
        while 1:
            tracking.update()
    except KeyboardInterrupt:
        tracking.stop()
mainLoop()