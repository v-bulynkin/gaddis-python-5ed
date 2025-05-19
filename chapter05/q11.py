# Математический тест
def main():
	import random
	n1 = random.randint(1, 999)
	n2 = random.randint(1, 999)
	print(f'{n1:>6d}')
	print(f'+ {n2:>4d}')
	answer = int(input('Ваш ответ: '))
	check(n1,n2,answer)
def check(n1,n2,answer):
	right_answer = n1 + n2
	if answer == right_answer:
		print('Отлично, это правильный ответ!')
	else:
		print('Правильный ответ -', right_answer)
if __name__ == '__main__':
	main()
