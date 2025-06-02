# Гольф-клуб. Ввод имени игрока и его счёта в игре, добавление записи в файл

g_name = input('Имя игрока: ')
# Использование переменной в запросе input()
g_score = str(input("Счёт игрока {}: ".format(g_name)))
 
file = open(r'C:\temp\golf.txt', 'a')
 
file.write(f'{g_name}\n')
file.write(f'{g_score}\n')
file.close()
