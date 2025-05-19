### Выручка от продажи мест на стадионе (стоимость: А - 20, B - 15, C - 10)
def main():
	sold_a = int(input('Продано мест А: '))
	sold_b = int(input('Продано мест B: '))
	sold_c = int(input('Продано мест C: '))
	print(f'Выручено: {income(sold_a,sold_b,sold_c)}')
def income(a,b,c):
	return a*20 + b*15 + c*10
if __name__ == '__main__':
	main()
