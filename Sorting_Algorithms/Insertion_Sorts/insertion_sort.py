def insertion_sort(array):
	#iterate for how man elements there are in array
	for i in range(1, len(array)):
		print(array)

		key = array[i]
		follow = i-1

		#if key < follow
		#set follow to one more than itself(which would be the key on first iter and the first follow on second)
		#once we hit one that isnt greater than key we stop and set key ahead of it
		while follow >= 0 and key < array[follow]:
			array[follow+1] = array[follow]
			follow -= 1
			print(array)
		#here is where we put the key 
		array[follow+1] = key 


array = [1,12,14,2,9,11]
insertion_sort(array)

print(array)


"""
[1, 12, 14, 2, 9, 11] 	origional

[1, 12, 14, 2, 9, 11] 	key = 12 follow = 1, array[follow+1] = key 

[1, 12, 14, 2, 9, 11] 	key = 14 follow = 12 #next key array[follow+1] = key 

[1, 12, 14, 14, 9, 11] 	key = 2 follow = 14, follow[i+1] = follow[]

[1, 12, 12, 14, 9, 11]	key = 2 follow = 12, follow[i+1] = follow[] 	

[1, 2, 12, 14, 9, 11]	key = 2 follow = 1, array[follow+1] = key

[1, 2, 12, 14, 14, 11] 

[1, 2, 12, 12, 14, 11]

[1, 2, 9, 12, 14, 11]

[1, 2, 9, 12, 14, 14]

[1, 2, 9, 12, 12, 14]

[1, 2, 9, 11, 12, 14]

"""