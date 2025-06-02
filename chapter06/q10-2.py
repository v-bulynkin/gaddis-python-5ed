# Гольф-клуб. Чтение имён игроков и их счёта из файла

file = open(r'C:\temp\golf.txt', 'r')

s = file.readline().rstrip('\n')
while s != '':
	print('Игрок:', s)
	print('Счёт:', file.readline().rstrip('\n'))
	s = file.readline().rstrip('\n')
file.close()
