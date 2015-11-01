import random

class Cell:

	def __init__(self,width,height,numCells):
		self.width = width
		self.height = height
		self.cellsParent = [ [0 for i in range(0,width)] for i in range(0,height) ]
		self.cellsChild = [ [0 for i in range(0,width)] for i in range(0,height) ]
		if width < 3 or height < 3:
			print "Maybe longer width and height"
		elif numCells > width * height:
			print "too much cells"
		else:
			for y in range(0, height):
				for x in range(0, width):
					if numCells > 0:
						self.cellsParent[y][x] = 1
						numCells -= 1
					else:
						self.cellsParent[y][x] = 0
			x = 4
			while(x > 0):
				self.cellsParent = map(list, zip(*self.cellsParent))
				for i in range(0, height):
					random.shuffle(self.cellsParent[i])
				x -= 1

	def countNeighbors(self,y,x):
		count = 0;
		for i in range(y-1,y+2):
			for j in range(x-1,x+2):
				if (i == -1 or i == 10 or j == -1 or j == 10):
					pass
				elif (i == y and j == x):
					pass

				elif self.cellsParent[i][j] == 1:
					#print "self.cellsParent[%d][%d]: %d" %(i,j,self.cellsParent[i][j])
					count = count + 1
					#print "+1"
					pass
		return count

	def toSurvive(self,y,x):
		#is living
		if self.cellsParent[y][x] == 1:
			num = self.countNeighbors(y,x)
			if num in [0, 1, 4]:
				return False
			else:
				return True
		#is dead
		elif self.cellsParent[y][x] == 0:
			num = self.countNeighbors(y,x)
			if num == 3:
				return True
			else:
				return False

	def tick(self):
		for i in range(0,10):
			for j in range(0,10):
				if self.toSurvive(i,j) == True:
					self.cellsChild[i][j] = 1
				else:
					self.cellsChild[i][j] = 0

def draw(array):
	y = 0
	print "----------"
	print " ",
	print ""
	for row in array:
		#print y,
		for item in row:
			if item == 0:
				print '_',
			else: 
				print '*',
		print ""
		y += 1

cell = Cell(10,10,20)
draw(cell.cellsParent)
g = 10
while(g):
	cell.tick()
	cell.cellsParent = cell.cellsChild
	draw(cell.cellsParent)
	# print "generation: %d" %g
	g -= 1