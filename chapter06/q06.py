# Вычислить среднее арифметическое чисел в файле

file = open(r'C:\temp\40-random-numbers.txt', 'r')
c = 0.0
div = 0
for i in file:
	c += float(i)
	div += 1
file.close()

print('Среднее арифметическое всех чисел в файле:', c / div)
