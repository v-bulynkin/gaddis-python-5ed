# Вычисление среднего кол-ва шагов в месяц из файла с 365-ю записями.

jan = ['Январь', 31]
feb = ['Февраль', 28]
mar = ['Март', 31]
apr = ['Апрель', 30]
may = ['Май', 31]
jun = ['Июнь', 30]
jul = ['Июль', 31]
aug = ['Август', 31]
sep = ['Сентябрь', 30]
oct = ['Октябрь', 31]
nov = ['Ноябрь', 30]
dec = ['Декабрь', 31]

file = open(r'C:\temp\steps.txt', 'r')

for month in [jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec]:
	steps = 0
	for day in range(int(month[1])):
		s = file.readline().rstrip('\n')
		steps += int(s)
		
	print(f'Всего шагов ({month[0]}): {steps}')
	print(f'Среднее кол-во шагов ({month[0]}): {int(steps / month[1])}')

file.close()
