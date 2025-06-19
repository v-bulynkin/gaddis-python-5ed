# Генератор лотерейных чисел

NUMBERS_COUNT = 7

def main():
	numbers = generate_numbers()
	print_numbers(numbers)

def generate_numbers():
	import random
	numbers = []
	for i in range(NUMBERS_COUNT):
		numbers.append(random.randint(0,9))	
	return numbers

def print_numbers(numbers):
	for i in numbers:
		print(i, end='')

if __name__ == '__main__':
	main()
