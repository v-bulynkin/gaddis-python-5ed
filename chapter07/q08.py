# Поиск имён в списках популярных

def main():
	boy_names = get_names(r'C:\temp\BoyNames.txt')
	girl_names = get_names(r'C:\temp\GirlNames.txt')
	my_names = (input('Введите имена, разделённые пробелами, которые вы хотите проверить: ')).split()
	my_list = clean_list(my_names)

	for i in my_list:
		if i in boy_names:
			print(f'Имя {i} есть в списке популярных имён мальчиков')
		elif i in girl_names:
			print(f'Имя {i} есть в списке популярных имён девочек')
		else:
			print(f'Имени {i} нет в списках популярных имён')
	
def get_names(file_path):
	names_file = open(file_path, 'r')
	names_raw = names_file.readlines()
	names_file.close()
	names_list = [i.rstrip('\n') for i in names_raw]
	return names_list
	
def clean_list(my_list):
	l = []
	for i in my_list:
		if i != '':
			l.append(i)
	return l
	
if __name__ == '__main__':
	main()

'''
Введите имена, разделённые пробелами, которые вы хотите проверить: Joseph    Olivia Stephanie   Benjamin               Scraper
Имя Joseph есть в списке популярных имён мальчиков
Имя Olivia есть в списке популярных имён девочек
Имя Stephanie есть в списке популярных имён девочек
Имя Benjamin есть в списке популярных имён мальчиков
Имени Scraper нет в списках популярных имён
'''
