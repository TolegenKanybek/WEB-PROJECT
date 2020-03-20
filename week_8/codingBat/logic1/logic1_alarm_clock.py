def alarm_clock(day, vacation):
    if vacation:
        if is_weekday(day): return '10:00'
        else: return 'off'
    else:
        if is_weekday(day): return '7:00'
        else: return '10:00'




alarm_clock(1, False) 