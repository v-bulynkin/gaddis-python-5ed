# Показать количество имён в списке.

file = open(r'C:\temp\names.txt', 'r')
c = 0
for i in file:
	c += 1
file.close()

print('Файл содержит', c, 'имён.')
