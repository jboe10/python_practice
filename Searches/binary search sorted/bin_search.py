def BS(arr, x):

	middle = (len(arr)/2)
	mid = int(middle)
	print(mid)

	if len(arr) > 1:
		
		if x == arr[mid]:
			print("found")

		elif x > arr[mid]:
			print(">" + str(arr))
			BS(arr[mid:], x)

		else:
			print(">")
			BS(arr[:mid], x)
	else:
		if x == arr[mid]:
			print("found")
		else:
			print("not in list")


array = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
BS(array, 17)