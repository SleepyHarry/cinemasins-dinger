import pygame as pg
import os, sys, time, random, math
from useful import load_image, colors
from textFuncs import *

pg.mixer.pre_init(buffer=512)

pg.init()

size = width, height = 1920, 1080
fps_tgt = 30
clock = pg.time.Clock()

font = pg.font.SysFont("arial", 420, bold=True)

screen = pg.display.set_mode(size, pg.FULLSCREEN)

pg.mixer.init()
ding = pg.mixer.Sound(os.path.join(os.curdir, "resource", "ding.wav"))

word_text = textOutline(font, "Sins: ", white, black)
word_text_rect = word_text.get_rect(right=(4*width/7), centery=(height/2))

num_sins = 0

def sins_text(sins):
    text = textOutline(font, ' '+str(sins), white, black)

    return text, text.get_rect(left=(width/2), centery=(height/2))

text, text_rect = sins_text(0)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.MOUSEBUTTONDOWN:
            m1, m3, m2 = pg.mouse.get_pressed()
            mX, mY = pg.mouse.get_pos()

        if event.type == pg.KEYDOWN:
            keys = pg.key.get_pressed()

            if keys[pg.K_ESCAPE]:
                pg.quit()
                sys.exit()
            
            if keys[pg.K_SPACE]:
                ding.play()

                num_sins += 1

                text, text_rect = sins_text(num_sins)

            if keys[pg.K_r]:
                num_sins = 0

                text, text_rect = sins_text(0)

    screen.fill(colors.black)

    screen.blit(word_text, word_text_rect)
    screen.blit(text, text_rect)

    pg.display.flip()

    clock.tick(fps_tgt)
