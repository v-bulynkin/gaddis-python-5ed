# Вывести первые 5 строк текстового файла. Если строк меньше, вывести весь файл.

file_path = input('Input a path to text file: ')

file = open(file_path, 'r')
s = 'start'
c = 1
while s != '' and c <= 5:
	s = file.readline().rstrip('\n')
	print(s)
	c += 1
file.close()
