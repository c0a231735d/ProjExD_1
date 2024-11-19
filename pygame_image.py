import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))
def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    koukaton_img = pg.image.load("fig/3.png")
    koukaton_img = pg.transform.flip(koukaton_img, True, False)
    koukaton_rect = koukaton_img.get_rect()
    koukaton_rect.center = (300, 200)  
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        key_lst = pg.key.get_pressed()
        
        move_x, move_y = -1,0
        if key_lst[pg.K_UP]:    
            move_y = -1
        elif key_lst[pg.K_DOWN]:  
            move_y = 1 
        elif key_lst[pg.K_RIGHT]: 
            move_x = 1
        koukaton_rect.move_ip(move_x,move_y)
        
        x = -(tmr % 3200)
        screen.blit(bg_img, [x, 0])
        screen.blit(bg_img2, [x + 1600, 0])
        screen.blit(bg_img, [x + 3200, 0])
        screen.blit(bg_img2, [x + 4800, 0])
        screen.blit(koukaton_img, koukaton_rect)
        pg.display.update()
        tmr += 1
        clock.tick(200)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
