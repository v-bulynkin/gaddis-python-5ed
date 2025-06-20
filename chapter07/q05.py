# Проверка корректности номера расчётного счёта

def main():
	charge_accounts_file = open(r'C:\temp\charge_accounts.txt', 'r')
	charge_accounts_raw = charge_accounts_file.readlines()
	charge_accounts_file.close()
	charge_accounts = [int(i.rstrip('\n')) for i in charge_accounts_raw]

	my_account = int(input(f'Введите номер вашего счёта: '))
	if my_account in charge_accounts:
		print('Номер есть в списке.')
	else:
		print('Номера нет в списке!')

if __name__ == '__main__':
	main()
