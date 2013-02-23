import Image
from communications import SprayChalk

class StreetArtBot:
	width = 0
	height = 0

	def loadImage(this, fileName, maxWidth, maxHeight):
		im = Image.open(fileName) #mode=1 for black and white
		size = maxWidth, maxHeight
		im.thumbnail(size)
		this.width = im.size[0]
		this.height = im.size[1]
		this.pixels = [[0 for y in range(this.height)] for x in range(this.width)]
		for x in range(this.width):
			for y in range(this.height):
				point = x,y
				pixel = im.getpixel(point)
				if pixel[0]>=128:
					this.pixels[x][y]=1
					#print str(point) + " - " + str(this.width) + "," + str(this.height)
				else:
					this.pixels[x][y]=0

	def checkSpray(this, x, y):
		if x<=this.width and y<=this.height and this.pixels[x][y]==1:
			SprayChalk()
				
				
bot = StreetArtBot()
bot.loadImage("images/logo.png", 64, 64)
bot.checkSpray(32,15)
bot.checkSpray(63,22)