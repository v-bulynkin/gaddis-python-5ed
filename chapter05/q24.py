WIDTH = 300
HEIGHT = 300
START_X = -150
START_Y = -150

import turtle
indent_width = WIDTH / 10
indent_height =  HEIGHT / 10
def main():
	turtle.hideturtle()
	turtle.speed(0)
	turtle.up()
	turtle.goto(START_X,START_Y)
	turtle.down()
	drawPattern(WIDTH,HEIGHT,indent_width,indent_height)
	turtle.up()
	turtle.goto(START_X,START_Y)
	turtle.down()
	turtle.left(45)
	turtle.goto(START_X+WIDTH,START_Y+HEIGHT)
	turtle.goto(START_X,START_Y+HEIGHT)
	turtle.goto(START_X+WIDTH,START_Y)
	turtle.goto(START_X+WIDTH,START_Y+HEIGHT/2)
	turtle.goto(START_X,START_Y+HEIGHT/2)
	turtle.up()
	turtle.goto(START_X+WIDTH/2,START_Y)
	turtle.down()
	turtle.goto(START_X+WIDTH/2,START_Y+HEIGHT)
	turtle.done()
def drawPattern(w,h,indent_width,indent_height):
	for i in [False, False, True]:
		drawRectangle(w,h,i)
		turtle.goto(turtle.xcor()+indent_width,turtle.ycor()+indent_height)
		w = w-indent_width*2
		h = h-indent_height*2
def drawRectangle(w,h,fill):
	if fill == True:
		turtle.fillcolor()
		turtle.begin_fill()
	for i in [w, h, w, h]:
		turtle.forward(i)
		turtle.left(90)
	if fill == True:
		turtle.end_fill()
if __name__ == '__main__':
	main()
