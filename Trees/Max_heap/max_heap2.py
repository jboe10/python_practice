class node:

	def __init__(self, value = None, color = "black"):
		self.value = value
		self.left  = None
		self.right = None
		self.color = color


class red_black:

	def __init__(self):
		self.root = None


	#this makes it so we dont have to worry about root/parent being empty
	def insert(self, value):
		if self.root == None:
			self.root = node(value)
		else:
			self._insert(value, self.root)		
    ######################################
	def _insert(self, value, cur_node):
        #insert left obj if less than
		if value < cur_node.value:
			if cur_node.left == None:
				if cur_node.color == "black":
					cur_node.left = node(value, "red")
				else:
					cur_node.left = node(value)
			else:
				self._insert(value, cur_node.left)
		#insert right of object if greater than
		elif value > cur_node.value:
			if cur_node.right == None:
				if cur_node.color == "black":
					cur_node.right = node(value, "red")
				else:
					cur_node.right = node(value)
			else:
				self._insert(value, cur_node.right)
		else: 
			print("value in tree")


	def print_tree(self):
		self._print_tree(self.root)
    ####################################
	def _print_tree(self, current_node):
		if current_node != None:
			print(str(current_node.value) + " " + current_node.color)
			self._print_tree(current_node.left)
			self._print_tree(current_node.right)

			
heap = red_black()
heap.insert(1)
heap.insert(2)
heap.insert(3)
heap.insert(4)
heap.insert(5)
heap.insert(6)
heap.insert(7)
heap.insert(8)

heap.print_tree()





#root is black ------------
#all NIL are black---------
#if a node is red children are black