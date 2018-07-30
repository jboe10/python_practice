class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

class Linked_List_Sorted:

	def __init__(self):
		self.root = None

	def insert_ordered(self, data):
		if self.root == None:
			self.root = Node(data)
		elif(self.root.data > data):
			temp_root = self.root
			self.root = Node(data)
			self.root.next = temp_root
		else:
			self._insert_ordered(data, self.root)

	def _insert_ordered(self, data, current_node):
		if current_node.next != None:

			# Handles an insert inbetween to existing nodes
			if (current_node.data < data and current_node.next.data > data) or (current_node.data == data and current_node.next != None):
		
				new_node = Node(data)
				new_node.next = current_node.next
				current_node.next = new_node

			else:
				self._insert_ordered(data, current_node.next)
		else:
			print("we went here")
			current_node.next = Node(data)


	# appends node to begenning of list 
	def append_root(self,data):
		new_node = self.root
		self.root = Node(data)
		self.root.next = new_node

	def print_list(self):
		print(str(self.root.data) + " ")
		if self.root.next != None:
			self._print_list(self.root.next)

	def _print_list(self,current_node):
		print(str(current_node.data) + " ")

		if current_node.next != None:
			self._print_list(current_node.next)


llist = Linked_List_Sorted()
llist.insert_ordered(5)
llist.insert_ordered(7)
llist.insert_ordered(8)
llist.insert_ordered(6)
llist.insert_ordered(4)
llist.insert_ordered(3)


llist.print_list()


