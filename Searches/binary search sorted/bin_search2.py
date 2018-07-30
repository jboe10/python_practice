def bin_search(array,x):
	middle = int(len(array)/2)

	if len(array) > 1:
		if array[middle] == x:
			print("found at " + str(middle))
		elif x > array[middle]:
			bin_search(array[middle:], x)
		else:
			bin_search(array[:middle], x)
	else:
		if array[0] == x:
			print("found at " + str(middle))
		else:
			print("not found")

array2 = [1,2,3,3,5,6,7,8,10,11]
bin_search(array2, 1)