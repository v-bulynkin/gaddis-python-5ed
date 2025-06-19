# Общий объём продаж за неделю

def main():
	sales = enter_income()
	overall = count_sales(sales)
	print(f'Выручка за неделю составляет {overall:.2f}')

def enter_income():
	days = ['Пн','Вт','Ср','Чт','Пт','Сб','Вс']
	sales = []
	for i in days:
		day_income = float(input(f'Выручка за день ({i}): '))
		sales.append(day_income)	
	return sales

def count_sales(sales):
	overall = 0
	for i in sales:
		overall += i
	return overall
	
if __name__ == '__main__':
	main()
 
'''
Выручка за день (Пн): 2.3
Выручка за день (Вт): 4
Выручка за день (Ср): 5
Выручка за день (Чт): 3
Выручка за день (Пт): 6
Выручка за день (Сб): 7
Выручка за день (Вс): 6.1
Выручка за неделю составляет 33.40
''' 
