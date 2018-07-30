def insertion_sort(array):
	for i in range(1, len(array)):
		key = array[i]
		follow = i -1

		while follow >= 0 and key < array[follow]:
			array[follow+1] = array[follow]
			follow -= 1

		array[follow+1] = key

array = [12, 2,124,44,22,1,3,2]
insertion_sort(array)
print(array)