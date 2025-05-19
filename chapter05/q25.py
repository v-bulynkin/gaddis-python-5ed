# Шахматная доска
SQUARES_WIDTH = 8   # Кол-во клеток в ряду
SQUARES_HEIGHT = 8  # Кол-во рядов клеток
SQUARE_SIDE = 30    # Размер клетки

import turtle
def main():
	turtle.hideturtle()
	turtle.speed(0)
	x = 0
	y = 0
	fill = True
	for i in range(SQUARES_HEIGHT):
		for i in range(SQUARES_WIDTH):
			drawRectangle(fill)
			turtle.goto(turtle.xcor()+SQUARE_SIDE,turtle.ycor())
			# Не переключать, если чётное кол-во клеток в ряду и это последняя клетка,
      # чтобы новый ряд начинать с того же цвета
			if SQUARES_WIDTH % 2 == 0 and i == SQUARES_WIDTH-1:
				continue
			if fill == True:
				fill = False
			else:
				fill = True
		turtle.up()
		y += SQUARE_SIDE
		turtle.goto(x,y)
		turtle.down()
	turtle.done()
def drawRectangle(fill):
	if fill == True:
		turtle.fillcolor()
		turtle.begin_fill()
	for i in range(4):
		turtle.forward(SQUARE_SIDE)
		turtle.left(90)
	if fill == True:
		turtle.end_fill()
if __name__ == '__main__':
	main()
