def interpolation_serach(arr, n, x):
	lo = 0 
	hi = n - 1

	while lo <= hi and x >= arr[lo] and x <= arr[hi]:

		#formula to determine where best to put next marker
		pos = lo + int(((float(hi - lo)/(arr[hi] - arr[lo])) * (x-arr[lo])))

		if arr[pos] == x:
			return pos

		if arr[pos] < x:
			lo = pos + 1

		else:
			hi = pos -1

	return -1 

array = [10,12,14,16,17,22,25,26,39]
index = interpolation_serach(array,len(array),26)

print(index)