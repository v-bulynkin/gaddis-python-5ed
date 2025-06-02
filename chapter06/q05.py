# Прочесть файл с числами и сложить их.

file = open(r'C:\temp\40-random-numbers.txt', 'r')
c = 0.0
for i in file:
	c += float(i)
file.close()

print('Сумма всех чисел в файле:', c)


'''
What Every Programmer Should Know About Floating-Point Arithmetic
or
Why don’t my numbers add up?

So you’ve written some absurdly simple code, say for example:
	0.1 + 0.2
and got a really unexpected result:
	0.30000000000000004

https://floating-point-gui.de/
'''
