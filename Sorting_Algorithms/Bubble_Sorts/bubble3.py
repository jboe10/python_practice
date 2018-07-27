def bubble_sort(array):

	for i in array:
		checker = True
		for j in range(0,len(array) -1):
			if(array[j] > array[j+1]):
				checker = False
				temp = array[j]
				array[j] = array[j+1]
				array[j+1] = temp
		if checker == True:
			break

lists = [ 1 ,22, 33, 44, 22, 27, 39]
bubble_sort(lists)
print(lists)