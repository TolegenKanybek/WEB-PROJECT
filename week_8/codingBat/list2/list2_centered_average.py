def centered_average(nums):
    maxi = nums[0]
	mini = nums[0]
	sum = nums[0]
	for i in range(len(nums)):
		sum  =sum+ nums[i]
		if nums[i] > maxi:
			maxi = nums[i]
		elif nums[i] < mini:
			mini = nums[i]
	return (sum-maxi-mini) / (len(nums) - 2)



centered_average([1, 2, 3, 4, 100])