def typeconvo(newdf):
    newdf.day = newdf.day.apply(day)
    return newdf

def day(value):
    if value == 'Mon' or 'Monday' or 'mon' or 'monday':
        return 0
    elif value =='Tues' or 'Tuesday' or 'tues' or 'tuesday':
        return 1
    elif value == 'Wed' or 'Wednesday' or 'wed' or 'wednesday':
        return 2
    elif value == 'Thurs' or 'Thursday' or 'thurs' or 'Thursday':
        return 3
    elif value == 'Fri' or 'Friday' or 'fri' or 'friday':
        return 4
    elif value == 'Sat' or 'Saturday' or 'sat' or 'saturday':
        return 5
    elif value == 'Sun' or 'Sunday' or 'sun' or 'sunday':
        return 6

