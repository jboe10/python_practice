def insertion_sort(array):
	for i in range(1,len(array)):
	
		key = array[i]
		follow = i - 1 

		while i > 0 and key < array[follow]:
			array[follow+1] = array[follow]
			follow -= 1
		array[follow+1] = key

array = [1,12,14,2,9,11]
insertion_sort(array)

print(array)