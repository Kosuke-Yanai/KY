import sys
from math import floor
from random import randint
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN

# global variable declaration
WIDTH  = 4
HEIGHT = 4
SIZE   = 50

NONE   = 2
BLACK  = -1
WHITE  = 1

CHECKED = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode([WIDTH*SIZE, HEIGHT*SIZE])
FPSCLOCK = pygame.time.Clock()

def rvs_chk(field, x_pos, y_pos):
    """ 周囲の反転対象のマスを捜索 """
    for yoffset in range(-1, 2):
        for xoffset in range(-1, 2):
            xpos, ypos = (x_pos + xoffset, y_pos + yoffset)
            if 0 <= xpos < WIDTH and 0 <= ypos < HEIGHT and \
                field[ypos][xpos] + field[y_pos][x_pos] == 0:
                CHECKED[ypos][xpos] = True
                xpos_diff, ypos_diff = ((xpos - x_pos), (ypos - y_pos))
   
                CHECK_FLUG = 0
                xpos_2, ypos_2 = (xpos + xpos_diff, ypos + ypos_diff)
             
                while (0 <= xpos_2 < WIDTH and 0 <= ypos_2 < HEIGHT and CHECK_FLUG == 0):
                    if field[ypos_2][xpos_2] == field[ypos][xpos]:
                        CHECKED[ypos_2][xpos_2] = True
                        xpos_2, ypos_2 = (xpos_2 + xpos_diff, 
                                          ypos_2 + ypos_diff)
                    elif field[ypos_2][xpos_2] == NONE:
                        for del_y in range(0, HEIGHT, 1):
                            for del_x in range(0, WIDTH, 1):
                                CHECKED[del_y][del_x] = False
                        CHECK_FLUG = 1
                    else:
                        for rev_y in range(0, HEIGHT, 1):
                            for rev_x in range(0, WIDTH, 1):
                                if CHECKED[rev_y][rev_x] == True:
                                    CHECKED[rev_y][rev_x] = False
                                    field[rev_y][rev_x] = field[rev_y][rev_x] * (-1)
                        CHECK_FLUG = 1      
                
def main():
    """ メインルーチン """
    smallfont = pygame.font.SysFont(None, 36)
    largefont = pygame.font.SysFont(None, 72)
    message_white = largefont.render("!!WHITE WIN!!",
                                     True, (0, 255, 225))
    message_black = largefont.render("!!BLACK WIN!!",
                                    True, (0, 255, 225))
    message_draw = largefont.render("!!DRAW!!",
                                    True, (0, 255, 225))
    message_rect_w = message_white.get_rect()
    message_rect_w.center = (WIDTH*SIZE/2, HEIGHT*SIZE/2)
    message_rect_b = message_black.get_rect()
    message_rect_b.center = (WIDTH*SIZE/2, HEIGHT*SIZE/2)
    message_rect_d = message_draw.get_rect()
    message_rect_d.center = (WIDTH*SIZE/2, HEIGHT*SIZE/2)

    field = [[NONE for xpos in range(WIDTH)]
             for ypos in range(HEIGHT)]
 
    # 初期駒の配置
    for init_y in range(int(HEIGHT / 2) - 1, int(HEIGHT / 2) + 1, 1):
        for init_x in range(int(WIDTH / 2) - 1, int(WIDTH / 2) + 1, 1):
            if init_y == init_x:
                field[init_y][init_x] = -1
            else:
                field[init_y][init_x] = 1
          
    turn_count = 0
    
    while True:        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and \
                event.button == 1:
                xpos, ypos = floor(event.pos[0] / SIZE),\
                             floor(event.pos[1] / SIZE)
                if field[ypos][xpos] == NONE:
                    turn_count += 1
                    if (turn_count % 2 ) == 0:
                        field[ypos][xpos] = -1
                        rvs_chk(field, xpos, ypos)
                    else:
                        field[ypos][xpos] = 1
                        rvs_chk(field, xpos, ypos)

        # 描画
        SURFACE.fill((0, 96, 0))
        for ypos in range(HEIGHT):
            for xpos in range(WIDTH):
                tile = field[ypos][xpos]
                rect = (xpos*SIZE, ypos*SIZE, SIZE, SIZE)

                if tile == WHITE:
                    pygame.draw.ellipse(SURFACE, (0, 0, 0), rect)
                elif tile == BLACK:
                    pygame.draw.ellipse(SURFACE, (255, 255, 255), rect)

        # 線の描画
        for index in range(0, WIDTH*SIZE, SIZE):
            pygame.draw.line(SURFACE, (96, 96, 96),
                             (index, 0), (index, HEIGHT*SIZE))
        for index in range(0, HEIGHT*SIZE, SIZE):
            pygame.draw.line(SURFACE, (96, 96, 96),
                             (0, index), (WIDTH*SIZE, index))

        # メッセージの描画
        if turn_count == ((WIDTH * HEIGHT) - 4):
            for count_y in range(0, HEIGHT, 1):
                for count_x in range(0, WIDTH, 1):
                    if field[count_y][count_x] == 1:
                        white_num = 1
                    else:
                        black_num = 1

            if white_num > black_num:
                SURFACE.blit(message_white, message_rect_w.topleft)
            elif white_num < black_num:
                SURFACE.blit(message_black, message_rect_b.topleft)
            else:
                SURFACE.blit(message_draw, message_rect_d.topleft)         

        pygame.display.update()
        FPSCLOCK.tick(15)

if __name__ == '__main__':
    main()

