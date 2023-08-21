def converter(hour, min, period):
    if hour < 1 or hour > 12 or min < 0 or min > 59 or (period != "am" and period != "pm"):
        print("Invalid input. Hour: 1-12, Min: 0-59, Period: am/pm")
        return "Invalid input. Hour: 1-12, Min: 0-59, Period: am/pm"
    else:
        if period == "am" and hour == 12:
            newHour = 0
        elif period == "am":
            newHour = hour
        elif period == "pm" and hour < 12:
            newHour = hour + 12
        else:
            newHour = hour
    
    time = f"{newHour:02d}{min:02d}"
    print(time)
    return time
converter(11,30,"pm")



