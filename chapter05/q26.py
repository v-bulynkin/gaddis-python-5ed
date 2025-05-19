# Городской силуэт
import turtle
def main():
	turtle.hideturtle()
	turtle.speed(0)
	x = 0
	y = 0
	turtle.fillcolor()
	turtle.begin_fill()
  # Холст
	for i in range(4):
		turtle.forward(400)
		turtle.left(90)
	turtle.end_fill()
	stars(x,y)
	buildings(x,y)
	windows(x,y)
	turtle.done()
def stars(x,y):
	import random
  # 100 звёзд
	for i in range(100):
		turtle.up()
		turtle.goto(x,y)
		turtle.goto(x+random.randint(1,400),y+random.randint(1,400))
		turtle.down()
		turtle.dot(3, 'white')
def windows(x,y):
	window(50,150)
	window(90,320)
	window(90,300)
	window(130,100)
	window(150,260)
	window(250,230)
def window(x,y):
	turtle.up()
	turtle.goto(x,y)
	turtle.setheading(0)
	turtle.down()
	turtle.color('yellow')
	turtle.begin_fill()
	for i in range(4):
		turtle.forward(15)
		turtle.left(90)
	turtle.end_fill()
def buildings(x,y):
	turtle.up()
	turtle.goto(x,y+120)
	turtle.down()
	turtle.color('gray')
	turtle.begin_fill()
	turtle.forward(40) # >
	turtle.left(90)
	turtle.forward(60) # ^
	turtle.right(90)
	turtle.forward(40) # >
	turtle.left(90)
	turtle.forward(170) # ^
	turtle.right(90)
	turtle.forward(100) # >
	turtle.right(90)
	turtle.forward(190) # вниз
	turtle.left(90)
	turtle.forward(60) # >
	turtle.left(90)
	turtle.forward(100) # ^
	turtle.right(90)
	turtle.forward(90) # >
	turtle.right(90)
	turtle.forward(80) # вниз
	turtle.left(90)
	turtle.forward(30) # >
	turtle.right(90)
	turtle.forward(80) # вниз
	turtle.left(90)
	turtle.forward(40) # >
	turtle.goto(x+400,y)
	turtle.goto(x,y)
	turtle.goto(x,y+120)
	turtle.end_fill()
if __name__ == '__main__':
	main()
