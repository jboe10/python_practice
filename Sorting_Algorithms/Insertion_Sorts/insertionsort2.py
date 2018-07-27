def insertion_sort(array):
	print(array)
	for i in range(1,len(array)):

		key = array[i]
		follower = i - 1

		while follower >= 0 and key < array[follower]:
			array[follower+1] = array[follower]
			follower -= 1
			print(array)

		array[follower +1] = key

array = [1,12,14,2,9,11]
insertion_sort(array)

print(array)