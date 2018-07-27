def bubblesort(array):
	for i in array:
		print(array)
		swap = False
		for j in range(len(array) -1):
			if array[j] > array[j+1]:
				swap = True

				temp = array[j]
				array[j] = array[j+1]
				array[j+1] = temp

		if swap == False:
			break


array = [1, 3, 11, 2, 3, 4, 33, 10]
bubblesort(array)