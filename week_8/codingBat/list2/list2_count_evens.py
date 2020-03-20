def count_evens(nums):
	count = 0
	for i in range(len(num)):
		if nums[i] % 2 == 0:
			count=count+1
	return count


count_evens([2, 1, 2, 3, 4])
