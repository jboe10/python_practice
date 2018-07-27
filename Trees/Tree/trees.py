class Tree:
	def __init__ (self, data = None):
		self.value = data
		self.right = None
		self.left  = None

	def add_left(self, data):
		self.left = Tree(data)

	def add_right(self, data):
		self.right = Tree(data)

	def transversal(self):
		if(self.left != None):	
			self.left.transversal()
		print(self.value)
		if(self.right != None):
			self.right.transversal()



root.transversal()