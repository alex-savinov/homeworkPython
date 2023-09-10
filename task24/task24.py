# -*- coding: cp1251 -*-
"""
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
Она растёт на круглой грядке, причём кусты высажены только по окружности. 
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может 
собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
"""

def func_blueberries(bush, blueberries):
    sum_blueberries_bush = []
    sum_buffer = 0
    i = 0
    if bush > 2:
        while (i < bush):
            if (i != bush - 1):
                sum_buffer = blueberries[i] + blueberries[i - 1] + blueberries[i + 1]
            else:
                sum_buffer = blueberries[i] + blueberries[i -1] + blueberries[0]
            sum_blueberries_bush.append( sum_buffer)
            i += 1
        sum_blueberries_bush.sort(reverse = True)
        print(f"Максимальное число ягод за один сбор: {sum_blueberries_bush[0]}")
    else:
        for k in range(bush):
            sum_buffer = sum_buffer + blueberries[k]
        print(f"Максимальное число ягод за один сбор: {sum_buffer}")

import random
bush = int(input("Введите количество кустов: "))
blueberries = list(random.randint(0, 10) for i in range(bush))
print(blueberries)
func_blueberries(bush,blueberries)
