# Вывод чисел из списка, которые больше указанного числа n

def main():
	num_list = get_list('C:\\temp\\random-numbers.txt')
	n = int(input(f'Введите число: '))
	for i in num_list:
		if i > n:
			print(i)

def get_list(file_path):
	num_file = open(file_path, 'r')
	num_raw = num_file.readlines()
	num_file.close()
	num_list = [int(i.rstrip('\n')) for i in num_raw]
	return num_list
	
if __name__ == '__main__':
	main()

'''
Введите число: 89
90
98
96
90
93
93
98
92
97
99
97
90
92
'''
