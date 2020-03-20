def near_ten(num):
    mod10 = num % 10
    return (mod10 <= 2) or (mod10 >=8)


near_ten(12) 