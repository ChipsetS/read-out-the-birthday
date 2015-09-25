months = [ 'Janruary', 'Februry', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
'November', 'December' ] + 1000['wrong'] endings = ['st', 'nd', 'rd'] + 17['th'] + ['st', 'nd', 'rd'] + 7['th'] + ['st'] + 1000['wrong']
year = input("year: ") month = input("month: ") day = input("day： ")
month_number = int(month) day_number = int(day)
month_name = months[month_number-1] day_name = day + endings[day_number-1]
print(year + ', ' + month_name + ', ' + day_name) b = input('press any key to end ')
