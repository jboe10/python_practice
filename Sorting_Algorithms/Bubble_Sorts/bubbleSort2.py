def bubbleSort(array):


	for i in array:
		swapped = False
		for j  in range(len(array)-1):
			if (array[j] > array[j+1]):
				temp = array[j]
				array[j] = array[j+1]
				array[j+1] = temp
				swapped = True
		if swapped == False:
			break
			break
			




array = [1, 3, 9, 2, 9, 0, 10]

bubbleSort(array)

print(array)


