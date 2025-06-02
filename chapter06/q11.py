# Генератор веб-страницы

my_name = input('Введите своё имя: ')
my_desc = input('Расскажите о себе: ') 

file = open(r'C:\temp\index.html', 'w')

file.write('<html>\n<head>\n</head>\n<body>\n')
file.write(f'\t<center>\n\t\t<h1>{my_name}</h1>\n\t</center>\n')
file.write(f'\t<hr />\n\t{my_desc}\n\t<hr />\n')
file.write('</body>\n</html>\n')
file.close()
