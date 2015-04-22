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

num_sins = 0

def sins_text(sins):
    text = textOutline(font, "Sins: " + str(sins),
                        white, black)

    return text, text.get_rect(center=(width/2, height/2))

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

    screen.fill(colors.black)

    screen.blit(text, text_rect)

    pg.display.flip()

    clock.tick(fps_tgt)
