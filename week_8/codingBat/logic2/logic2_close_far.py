import Math
def close_far(a, b, c):
	return (Math.abs(b-a) <= 1 and Math.abs(c-a) >= 2 and Math.abs(c-b) >= 2
		or Math.abs(c-a) <= 1 and Math.abs(b-a) >= 2 and Math.abs(b-c) >= 2)


close_far(1, 2, 10) 