# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
n = int(input('Введите степень: '))

for i in range(n,-1,-1):
    k = random.randint(0,101)

    if i == 0: 
        if k !=0: print(f' + {k} = 0')
        else: print(' = 0')
    elif i == 1:
        print(f'{k} * x', end = '')
    else:
        print(f'{k} * x^{i}', end = ' + ')
        
