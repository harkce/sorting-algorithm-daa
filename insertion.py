def insertionSort(arr):
	lenarr = len(arr)
	x = 0
	while x < lenarr:
		temp = arr[x]
		y = x - 1
		while (y >= 0) and (temp < arr[y]):
			arr[y + 1] = arr[y]
			y -= 1
		arr[y + 1] = temp
		x += 1
	return arr

print insertionSort([4,1,3,2])