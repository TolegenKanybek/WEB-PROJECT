def make_bricks(small, big, goal):
	max_big = goal/5
	if max_big <= big:
		goal -= max_big*5
	else:
		goal -= big*5
	if goal <= small:
		return True
	return False


make_bricks(3, 1, 8)