# Using the pygame library, draw a simple picture. 
# It can be anything you like, but you must use at least 2 different types of shapes and 3 different colors.
import pygame, sys
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((700,450))

while True:
  DISPLAYSURF.fill((255,255,255))
  pygame.draw.rect(DISPLAYSURF, (14, 139, 161), (100,210,200,200), border_radius=5)
  pygame.draw.polygon(DISPLAYSURF, (245, 210, 0), [(75,225),(325,225),(200,100)])
  pygame.draw.rect(DISPLAYSURF, (3, 6, 86), (175,335,45,75))
  pygame.draw.rect(DISPLAYSURF, (105, 46, 2), (420,335,30,80))
  pygame.draw.polygon(DISPLAYSURF, (72, 173, 2), [(375,335),(500,335),(435,270)])
  pygame.draw.polygon(DISPLAYSURF, (72, 173, 2), [(385,300),(490,300),(435,245)])
  pygame.draw.polygon(DISPLAYSURF, (72, 173, 2), [(390,270),(480,270),(435,220)])
  pygame.display.update()
  