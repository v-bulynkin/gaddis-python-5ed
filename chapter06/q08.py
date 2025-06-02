# Чтение файла с числами, сумма чисел и их количество

file = open(r'C:\temp\random-numbers.txt', 'r')

quantity = 0
my_sum = 0
for i in file:
	my_sum += int(i)
	quantity += 1
file.close()
print('Сумма чисел:', my_sum)
print('Кол-во чисел:', quantity)
