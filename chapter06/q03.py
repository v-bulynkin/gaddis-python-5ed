# Пронумеровать строки в тектовом файле, нумерация с единицы, формат - <номер>: <строка>

file_path = input('Input a path to text file: ')

file = open(file_path, 'r')
c = 1
for i in file:
	print(f'{c}: {i.rstrip('\n')}')
	c += 1
file.close()
