def BS2(arr, l, r, x):

	if r >= l:
		tmp = (r+l)/2
		mid = int(tmp)
		if arr[mid] == x:
	
			print("found element")
			if l == 0:
				pos = r +l
			else:
				pos = l
			print(" found at " + str(pos))
		elif x > arr[mid]:
			BS2(arr,mid+1, r, x)
		else:
			BS2(arr,l, mid-1, x)
	else:
		print("element not found")

array = [1,2,3,4,5,6,8,10]

BS2(array,0,len(array)-1, 1)