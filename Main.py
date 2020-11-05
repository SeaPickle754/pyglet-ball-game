import pyglet
from pyglet.gl import glClearColor
import math
import random

win_height = 600
win_width = 600

win = pyglet.window.Window(win_height, win_width, caption = "SuperBallChase")
glClearColor(255, 255, 255, 1.0)
drawing_batch = pyglet.graphics.Batch()
player_image = pyglet.image.load("player.png")
player = pyglet.sprite.Sprite(player_image, x = win_width / 2, y = win_height / 2, batch = drawing_batch)

ball_image = pyglet.image.load("ball.png")
ball = pyglet.sprite.Sprite(ball_image, x = win_width / 2, y = win_height / 2 + 100, batch = drawing_batch)


def distance(targetA, targetB):
	return math.sqrt((targetA.x-targetB.x)**2 + (targetA.y-targetB.y)**2)
def isCollision(targetA = ball, targetB = player):
	if distance(targetA, targetB) < 25:
		return True
	else:
		return False

@win.event
def on_key_press(key, modifiers):
	global score
	if key == pyglet.window.key.UP:
		player.y += 15
		if isCollision():
			ball.y += random.randint(1, 50)
			if ball.y > win_height or ball.y == win_height:
				exit()
			
	elif key == pyglet.window.key.DOWN:
		player.y -= 15
		if isCollision():
			ball.y -= random.randint(1, 50)
			if ball.y < 0 or ball.y == 0:
				exit()
			
	elif key == pyglet.window.key.LEFT:
		player.x -= 15
		if isCollision():
			ball.x -= random.randint(1, 50)
			if ball.x < 0 or ball.x == 0:
				exit()
	elif key == pyglet.window.key.RIGHT:
		player.x += 15
		if isCollision():
			ball.x += random.randint(1, 50)
			if ball.x > win_width or ball.x == win_width:
				exit()
	elif key == pyglet.window.key.Q:
		exit()

@win.event
def on_mouse_press(button, x, y, modifiers):
	exit()
@win.event
def on_draw():
	win.clear()
	drawing_batch.draw()

pyglet.app.run()
