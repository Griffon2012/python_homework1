# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).

# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = float(input('X = '))
y = float(input('Y = '))

result = None

if x > 0 and y > 0:
    result = 1
if x < 0 and y > 0:
    result = 2
if x < 0 and y < 0:
    result = 3
if x > 0 and y < 0:
    result = 4

print(result)
