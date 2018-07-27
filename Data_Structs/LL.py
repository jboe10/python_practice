class  Node:
	def __init__(self, data = None):
		self.data  = data
		self.next  = None

class LL:
	def __init__(self):
		self.head = Node()

	def append(self, data):
		new_node = Node(data)
		cur = self.head
		while cur.next != None:
			cur = cur.next
		cur.next = new_node

	def length(self):
		cur = self.head
		total = 0
		while cur.next != None:
			total += 1
			cur = cur.next
		return total

	def display(self):
		elems = []
		cur_node = self.head
		while(cur_node.next != None):
			cur_node = cur_node.next
			elems.append(cur_node.data)
		print(elems)

	def search(self, data):
		current = self.head
		while current != None:
			if current.data == data:
				return current
			current = current.next

	def insert(self, data, parent_value):
		new_node = Node(data)
		current = self.search(parent_value)
		next_node = current.next
		current.next = new_node
		new_node.next = next_node

	def delete(self, delete_value):
		current = self.head
		if current.data == delete_value:
			current.data == None
		else:
			parent = current
			current = current.next

			ticker = False
			while ticker == False:
				if current.data == delete_value:
					ticker = True
				else:
					parent = parent.next
					current = current.next

			parent.next = current.next





my_list = LL()


my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.append(1)
my_list.append(3)
my_list.append(9)
my_list.append(11)

my_list.display()
my_list.search(11)
my_list.search(12)
my_list.search(9)



my_list.delete(4)
my_list.display()




