def sum67(nums):
	sum = 0
	six_mode = False
    for i in range(len(num)):
		if(six_mode==True):
			if nums[i] == 7:
				six_mode = False
		elif nums[i] == 6:
			six_mode = True
		else:
			sum =sum + nums[i]
	return sum



sum67([1, 2, 2])