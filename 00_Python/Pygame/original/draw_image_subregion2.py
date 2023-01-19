"""draw_image_subregion2.py"""
import sys
import pygame
from pygame.locals import QUIT,
Rect, KEYDOWN, K_LEFT, K_RIGHT

pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode((300,200))
FPSCLOCK = pygame.time.Clock()

def main():
  """main routine"""

  strip = pygame.image.load("strip.png")

  while True:
    for event in pygame.event.get(QUIT):
      pygame.quit()
      sys.exit()

    SURFACE.fill((255, 255, 255))
    SURFACE.blit(logo, (0, 0))
    SURFACE.blit(logo, (250, 50), Rect(50, 50, 100, 100))

    pygame.display.update()
    FPSCLOCK.tick(30)

if __name__=='__main__':
  main()
