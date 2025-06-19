# Статистика ежемесячных осадков

def main():
	months = ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь']
	mm = enter_level(months)
	print('------------------')
	count_year(mm)
	max_month(months,mm)
	min_month(months,mm)

def enter_level(months):
	mm = []
	for i in months:
		level = int(input(f'Уровень осадков ({i}): '))
		mm.append(level)	
	return mm

def count_year(mm):
	overall = 0
	for i in mm:
		overall += i
	print(f'Всего осадков за год: {overall}')
	
def max_month(months,mm):
	max_index = mm.index(max(mm))
	print(f'Максимум осадков: {mm[max_index]} ({months[max_index]})')
	
def min_month(months,mm):
	min_index = mm.index(min(mm))
	print(f'Минимум осадков: {mm[min_index]} ({months[min_index]})')
	
if __name__ == '__main__':
	main()

'''
Уровень осадков (Январь): 57
Уровень осадков (Февраль): 67
Уровень осадков (Март): 9
Уровень осадков (Апрель): 47
Уровень осадков (Май): 37
Уровень осадков (Июнь): 196
Уровень осадков (Июль): 71
Уровень осадков (Август): 37
Уровень осадков (Сентябрь): 11
Уровень осадков (Октябрь): 89
Уровень осадков (Ноябрь): 79
Уровень осадков (Декабрь): 59
------------------
Всего осадков за год: 759
Максимум осадков: 196 (Июнь)
Минимум осадков: 9 (Март)
'''
