# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех
# значений предиката.

for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            var1 = not (bool(x) or bool(y) or bool(z))
            var2 = not (bool(x)) and not (bool(y)) and not (bool(z))
            print(
                f'¬(X ⋁ Y ⋁ Z) = {var1}, ¬X ⋀ ¬Y ⋀ ¬Z = {var2} итог {var1 == var2}')
