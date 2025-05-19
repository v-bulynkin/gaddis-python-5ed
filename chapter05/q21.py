# rock, paper, scissors game
def main():
	import random
	while True:
		comp = random.randint(1, 3)
		print('1. 🪨','2. ✂️','3. 📄',sep='\n')
		me = int(input('? '))
		tsuefa(me,comp)
def tsuefa(me,comp):
	if comp == me:
		print(f'(✋) {conv_num(me)} : {conv_num(comp)} (🖥️)')
		if __name__ == '__main__':
			main()
	elif (comp == 1 and me == 2) or (comp == 2 and me == 3) or (comp == 3 and me == 1):
		print(f'Вы проиграли! (✋) {conv_num(me)} : {conv_num(comp)} (🖥️)')
	else:
		print(f'Вы выиграли! (✋) {conv_num(me)} : {conv_num(comp)} (🖥️)')
def conv_num(n):
	if n == 1:
		out = '🪨'
	elif n == 2:
		out = '✂️'
	elif n == 3:
		out = '📄'
	return out
if __name__ == '__main__':
	main()
