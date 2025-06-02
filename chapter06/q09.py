# q06 с обработкой исключений IOError и ValueError

try:
	file = open(r'C:\temp\40-random-numbers.txt', 'r')
except IOError:
	print('Ошибка при открытии файла!')

c = 0.0
div = 0
for i in file:
	try:
		c += float(i)
	except ValueError:
		print('Неправильный тип данных, невозможно преобразовать в число!')
	div += 1
file.close()

print('Среднее арифметическое всех чисел в файле:', c / div)
