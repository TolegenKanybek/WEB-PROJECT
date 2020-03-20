def fix_teen(int n):
	if n < 13 or n > 19 or n == 15 |or n == 16:
		return n
	return 0


def no_teen_sum(a,b,c):
     return (fix_teen(a) + fix_teen(b) +fix_teen(c))



no_teen_sum(1, 2, 3) 