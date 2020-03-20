def caughtSpeeding(speed, is_birthday):
    if is_birthday: 
        if speed <= 65:
            return 0
        elif 66 <= speed and speed <= 85:
            return 1
         elif 86 <=  speed:
            return 2
    if speed <= 60:
        return 0
    elif 61 <= speed and speed <= 80:
        return 1
    else:
        return 2
    

caught_speeding(60, False)