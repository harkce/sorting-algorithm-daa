def selectionSort(arr):
	lenarr = len(arr)
	x = 0
	while x < lenarr:
		minidx = x
		y = x + 1
		while y < lenarr:
			if arr[y] < arr[minidx]: minidx = y
			y += 1
		arr[x], arr[minidx] = arr[minidx], arr[x]
		x += 1
	return arr

print selectionSort([4,1,3,2])