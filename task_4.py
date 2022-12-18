# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек
# в этой четверти (x и y).

number = int(input('Введите номер четверти: '))

if number == 1:
    result = 'x > 0, y > 0'
elif number == 2:
    result = 'x < 0, y > 0'
elif number == 3:
    result = 'x < 0, y < 0'
elif number == 4:
    result = 'x > 0, y < 0'
else:
    result = 'Нет такой четверти'
print(result)
