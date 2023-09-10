
start_value = int(input("¬ведите начальный элемент: "))
step_value = int(input("¬ведите шаг прогрессии: "))
count_step = int(input("¬ведите количество итераций: "))
print(*range(start_value,count_step * step_value + start_value,step_value))