# Простые числа
MY_RANGE=100
def main():
	#num = int(input('Введите число: '))
	#print(prime(num))
	print('Простые числа в диапазоне от 1 до', MY_RANGE)
	for i in range(MY_RANGE):
		p = prime(i+1)
		if p:
			print(i+1)
def prime(n):
	if n == 2:
		return True
	elif n%2 == 0 or n <=1:
		return False
	for i in range(3, int(n**0.5) + 1, 2):
		if n % i == 0:
			return False
	return True
if __name__ == '__main__':
	main()
  
