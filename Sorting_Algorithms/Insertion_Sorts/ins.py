def insertion_sort(array):
	for i in range(1, len(array)):

		key = array[i]
		follow = i -1 

		#key is less than follow, lets swap the cards
		#also make sure our boundray for follow exisits so we dont go out of bounds
		while follow >= 0 and key < array[follow]:
			#lets move the 
			array[follow+1] = array[follow]
			#iterate follow
			follow -= 1
			#print
			print(array)

		#now we put the key where the last follow was(we have the +1 cuz we decremented it)
		array[follow+1] = key


array = [1,3,20,13,4,9]
insertion_sort(array)
print(array)
