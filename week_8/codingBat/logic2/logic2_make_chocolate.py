def make_chocolate(small,big,goal):
	max_big = goal/5
	if max_big <= big:
		goal -= max_big*5
	else:
		goal -= big*5
	if goal <= small:
		return goal
	return -1

make_chocolate(4, 1, 9) 