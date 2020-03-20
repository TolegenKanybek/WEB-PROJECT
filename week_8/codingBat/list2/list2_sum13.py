def sum13(nums):
	sum = 0
	for i in range(len(num)):
		if nums[i] == 13:
			i=i+1
		else:
			sum =sum + nums[i]
	return sum


sum13([1, 2, 2, 1])