import Image
from communications import SprayChalk

class StreetArtBot:
	def loadImage(self, fileName, maxWidth, maxHeight):
		im = Image.open(fileName) #mode=1 for black and white
		size = maxWidth, maxHeight
		im.thumbnail(size)
		self.width = im.size[0]
		self.height = im.size[1]
		self.pixels = [[0 for y in range(self.height)] for x in range(self.width)]
		self.sprayed = [[0 for y in range(self.height)] for x in range(self.width)]
		for x in range(self.width):
			for y in range(self.height):
				point = x,y
				pixel = im.getpixel(point)
				if pixel[0]>=128:
					self.pixels[x][y]=1
					#print str(point) + " - " + str(self.width) + "," + str(self.height)
				else:
					self.pixels[x][y]=0

	def checkSpray(self, x, y):
		if x<=self.width and y<=self.height and self.pixels[x][y]==1 and self.sprayed[x][y]==0:
			SprayChalk()
			self.sprayed[x][y]==1
			
				
				
bot = StreetArtBot()
bot.loadImage("images/logo.png", 64, 64)
bot.checkSpray(32,15)
bot.checkSpray(63,22)