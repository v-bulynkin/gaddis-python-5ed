# random number guessing game
MY_RANGE = 100
def main():
	import random
	again = 'y'
	while again in ['y','Y','Д','д']:
		n = random.randint(1,MY_RANGE)
		my_n = int(input(f'Угадайте число от 1 до {MY_RANGE}: '))
		guess(n,my_n)
		again = input('Сыграем ещё? (ДдYy): ')
def guess(n,my_n):
	tries=1
	while my_n != n:
		tries += 1
		if my_n < n:
			my_n = int(input('Слишком мало, попробуйте ещё раз: '))
		elif my_n > n:
			my_n = int(input('Слишком много, попробуйте ещё раз: '))
	print(f'Поздравляю! Вы угадали с {tries}-й попытки.')
if __name__ == '__main__':
	main()
  
