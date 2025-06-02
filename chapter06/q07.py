# Запись файла со случайными числами в диапазоне от 1 до 500. Кол-во чисел задаётся.

file = open(r'C:\temp\random-numbers.txt', 'w')
how_many = int(input('Сколько чисел записывать в файл? '))

import random
for i in range(how_many):
	file.write(f'{str(random.randint(1, 500))}\n')
file.close()
