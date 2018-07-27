def sum_match(array, sums):
		left = 0
		right = len(array) - 1
		_sum_match(array, sums, left, right)

def _sum_match(array, sums, left, right):

		if(array[left] + array[right] == sums):
			print("Array @ index ",left," + Array at index ",
				right,"Equals",sums)
			print(array[left]," + ",array[right]," = ", sums)
		elif(left == right):
			print("no solution")
		elif(array[left] + array[right] < sums):
			_sum_match(array, sums, left + 1, right)
		elif(array[left] + array[right] > sums):
			_sum_match(array, sums, left, right - 1)




array = [1,2,4,4,6,7,8,9,11,12,15,18,19,22,34,36,49,56,59]

sum_match(array, 74)