number = input('введите число от 1 до 100\n')
number = int(number)
while number != 0:
    if number < 0 or number > 100:
        print('ошибка ввода вы ввели числа отличные от диапазона от 1 до 100')
        break
    elif number % 10 == 1 and number % 100 != 11:
        print(number, ' ворона')
    elif number % 10 > 1 and number % 10 < 5 and (number % 100 < 11 or number % 100 > 15):
        print(number, ' вороны')
    else:
        print(number, ' ворон')
    number -= 1
    