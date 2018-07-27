"""
MergeSort(arr[], l,  r)
If r > l
     1. Find the middle point to divide the array into two halves:  
             middle m = (l+r)/2
     2. Call mergeSort for first half:   
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)
""" 
def merge(array, t, m, r):
	n1 = m -t + 1
	n2 = r - m
	print(n1)
	print(n2)
	#populate arrays to hold halfs
	L = [0] * (n1)
	R = [0] * (n2)

	#copy data to tep array L[] and R[]
	for i in range(0, (n1)):
		L[i] = array[t + i]

	for j in range(0, (n2)):
		R[i] = array[m + 1 + j]

	#merge the temp array back into array[t..r]
	i = 0
	j = 0
	k = t

	while i < int(n1) and j < int(n2):
		if L[i] <= R[j]:
			array[k] = L[i]
			i += 1
		else:
			array[k] = R[j]
			j += 1

		k += 1

	#copy the remaining elements of l[], if there are any
	while i < n1:
		array[k] = L[i]
		i += 1
		k += 1

	#copy the remaining elemtns of R[], if there are any 
	while j < n2:
		array[k] = R[j]
		j += 1 
		k += 1

def mergeSort(array, t, r):
	if t < r:

		#same as (l+r) but avoids overflow of large l and h
		m = (t+(r-1))/2
		
		#sort first and second halves
		if(m>=1):
			print(m)
			mergeSort(array,t,int(m))
			mergeSort(array, int(m)+1, r)
			merge(array, t, int(m), r)


lists = [1,2,9,19,2,10]
x = len(lists) -1
mergeSort(lists,0, x)
print(lists)

















lists = [1, 5, 4, 9, 7, 2, 3, 1]
mergeSort(lists)