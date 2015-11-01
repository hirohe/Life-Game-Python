class Cell:
	def countNeighbors(self,y,x,array):
		count = 0;
		for i in range(y-1,y+2):
			for j in range(x-1,x+2):
				if (i == -1 or i == 10 or j == -1 or j == 10):
					pass
				elif (i == y and j == x):
					pass

				elif array[i][j] == 1:
					#print "array[%d][%d]: %d" %(i,j,array[i][j])
					count = count + 1
					#print "+1"
					pass
		return count

	def toSurvive(self,y,x,array):
		#is living
		if array[y][x] == 1:
			num = self.countNeighbors(y,x,array)
			if num in [0, 1, 4]:
				return False
			else:
				return True
		#is dead
		elif array[y][x] == 0:
			num = self.countNeighbors(y,x,array)
			if num == 3:
				return True
			else:
				return False

def draw(array):
	y = 0
	print "----------"
	print " ",
	for x in range(0,10):
		print x,
	print ""
	for row in array:
		print y,
		for item in row:
			if item == 0:
				print '~',
			else: 
				print '*',
		print ""
		y += 1

def tick(array):
	arrayChild = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
	cell = Cell()
	for i in range(0,10):
		for j in range(0,10):
			if cell.toSurvive(i,j,array) == True:
				arrayChild[i][j] = 1
			else:
				arrayChild[i][j] = 0
	return arrayChild

cellsParent = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
			   [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
			   [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
			   [1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
			   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

#cell = Cell()

#print cell.toSurvive(6,6,cells)
draw(cellsParent)
cellsChild =  tick(cellsParent)
g = 10
while(g):
	cellsParent = cellsChild
	draw(cellsParent)
	cellsChild =  tick(cellsParent)
	# print "generation: %d" %g
	g -= 1
