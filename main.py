import pygame as pg, sys
from pygame.locals import *
from random import randint

pg.init()

W = 800
s = pg.display.set_mode((W, W))
clock = pg.time.Clock()

RADIUS = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Particle:
    def __init__(self, color, x, y, dx, dy, radius):
        self.color = color
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius

    def draw(self):
        pg.draw.circle(s, self.color, (self.x, self.y), self.radius)


def color_generator():
    return [randint(100, 255) for _ in range(3)]

particle_list = []

for _ in range(100):
    new_particle = Particle(color_generator(), randint(RADIUS, W - RADIUS), randint(RADIUS, W - RADIUS), randint(1, 2), randint(1, 4), randint(1, 20))
    particle_list.append(new_particle)

def animate():
    pos = pg.mouse.get_pos()


    for p in particle_list:
        p.draw()
        if p.x + RADIUS > W or p.x - RADIUS < 0: p.dx = -p.dx
        if p.y + RADIUS > W or p.y - RADIUS < 0: p.dy = -p.dy
        p.x += p.dx
        p.y += p.dy

        if p.x > pos[0] > p.x:
            p.radius += 1

while True:
    s.fill(BLACK)
    animate()
    for e in pg.event.get():
        if e.type == QUIT:
            pg.quit()
            sys.exit()

    clock.tick(60)
    pg.display.update()


