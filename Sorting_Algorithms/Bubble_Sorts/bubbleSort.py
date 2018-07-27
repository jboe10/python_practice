def swap(array, key_pos):
	temp = array[key_pos+1]
	array[key_pos+1] = array[key_pos]
	array[key_pos] = temp


def bubble_sort(array):
	#needs a whole pass withouth swaps to 
	breaker = False
	for i in array:
		print(array)
		breaker = False
		for j in range(len(array) - 1):
			if(array[j] > array[j+1]):
				swap(array, j)
				breaker = True
		if breaker == False:
			break



array = [1, 3, 6, 2, 5, 6, 4, 9]

bubble_sort(array)
