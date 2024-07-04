"""draw_image1.py"""
import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((400,300))
FPSCLOCK = pygame.time.Clock()

def main():
  """main routine"""

  logo = pygame.image.load("python_logo.png")

  while True:
    for event in pygame.event.get(QUIT):
      pygame.quit()
      sys.exit()

    SURFACE.fill((255, 255, 255))

    # 左上が(20,50)の位置にロゴを描画
    SURFACE.blit(logo, (20, 50))

    pygame.display.update()
    FPSCLOCK.tick(30)

if __name__=='__main__':
  main()