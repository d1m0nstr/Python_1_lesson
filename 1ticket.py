tim = input('duration = ')
tim = int(tim)
min = 0
hour = 0
day = 0
if tim >= 86400:
    day = tim // 86400
    tim = tim % 86400
    print(day, 'дн')
if tim >= 3600:
    hour = tim // 3600
    tim = tim % 3600
    print(hour, 'час')
if tim >= 60:
    min = tim // 60
    tim = tim % 60
    print(min, 'мин')
print(tim, 'сек')
