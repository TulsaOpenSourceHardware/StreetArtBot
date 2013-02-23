import Image
from communications import SprayChalk

class ChalkBoard:
	def loadImage(self, fileName, maxWidth, maxHeight):
		im = Image.open(fileName) 
		size = maxWidth, maxHeight
		im.thumbnail(size)
		self.maxWidth = maxWidth
		self.maxHeight = maxHeight
		self.width = im.size[0]
		self.height = im.size[1]

#		self.black = [[0 for y in range(self.height)] for x in range(self.width)]
		self.colors = [[[0 for z in range(5)] for y in range(self.height)] for x in range(self.width)]				
		self.sprayed = [[[0 for z in range(5)] for y in range(self.height)] for x in range(self.width)]				
#		self.sprayed = [[0 for y in range(self.height)] for x in range(self.width)]

		for x in range(self.width):
			for y in range(self.height):
				point = x,y
				pixel = im.getpixel(point)
				cmyk = self.getCMYK(pixel[0], pixel[1], pixel[2])
				for c in range(4):
					if cmyk[c]>=0.5: self.colors[x][y][c]=1
				if pixel[0]>128: self.colors[x][y][4]=1

	# c - 0=Cyan, 1=Magenta, 2=Yellow, 3=Black, 4=Grayscale
	def checkSpray(self, xPercent, yPercent, c):
		x = int(xPercent * self.maxWidth)
		y = int(yPercent * self.maxHeight)
		#print str(y) + " - " + str(self.height)
		if x<self.width and y<self.height and self.colors[x][y][c]==1 and self.sprayed[x][y][c]==0:
			SprayChalk()
			self.sprayed[x][y][c]=1
			print "Spaying " + str(x) + "," + str(y) + " - " + str(xPercent) + "," + str(yPercent)


	def getCMYK(this, r,g,b):
		cmyk_scale = 100
		if (r == 0) and (g == 0) and (b == 0):
			# black
			return 0, 0, 0, cmyk_scale
		# rgb [0,255] -> cmy [0,1]
		c = 1 - r / 255.
		m = 1 - g / 255.
		y = 1 - b / 255.

		# extract out k [0,1]
		min_cmy = min(c, m, y)
		c = (c - min_cmy) / (1 - min_cmy)
		m = (m - min_cmy) / (1 - min_cmy)
		y = (y - min_cmy) / (1 - min_cmy)
		k = min_cmy

		# rescale to the range [0,cmyk_scale]
		return c*cmyk_scale, m*cmyk_scale, y*cmyk_scale, k*cmyk_scale
				
				
#bot = StreetArtBot()
#bot.loadImage("images/logo.png", 120, 90)

#bot.checkSpray(0.98, 0.50, 4)
#bot.checkSpray(0.98, 0.51, 4)

#for x in range(100):
#	for y in range(100):
#		bot.checkSpray(x/100.0, y/100.0, 4)