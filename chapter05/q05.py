### Оценочная стоимость и налог с недвижимости
def main():
	my_sum = float(input('Введите стоимость недвижимости: '))
	ocenochnaya_stoimost, nalog = tax(my_sum)
	print(f'Оценочная стоимость: {ocenochnaya_stoimost:.2f}')
	print(f'Налог: {nalog:.2f}')
def tax(s):
	# Оценочная стоимость - 60% от указанной
	ocenochnaya_stoimost = s * 0.6
	# 72 коп на каждые 100 руб от оценочной стоимости
	nalog = ocenochnaya_stoimost / 100 * 0.72
	return ocenochnaya_stoimost, nalog
if __name__ == '__main__':
	main()
